import re
from tkinter import E
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, User_Relationship, User_Profile
from . import db

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def dash():
    _user = session['id_user']
    return render_template('dashboard.html')


@views.route('/my-profile/change-color', methods=['GET', 'POST'])
@login_required
def change_color():
    _color = request.form.get('color')
    _user_profile = User_Profile.query.filter_by(id_user=session['id_user']).first()
    _user_profile.user_color_hex = _color
    db.session.commit()
    print(_user_profile.user_color_hex)
    return redirect(url_for('views.my_profile'))
        
@views.route('/my-profile')
@login_required
def my_profile():
    _user_id = session['id_user']
    # set current_user's visibility to the same as the user's profile
    _user = User.query.filter_by(id=_user_id).first()
    _user.visibility = User_Profile.query.filter_by(id_user=_user_id).first().profile_visibility

    # gets user's friends from User_Relationship
    # get all relationships containing both user's id
    _user_relationships = User_Relationship.query.filter((User_Relationship.id_user == _user_id) | (User_Relationship.id_friend == _user_id)).all()
    # +------------+
    # | id         |
    # | id_user    |
    # | id_friend  |
    # | is_pending |
    # +------------+
    pending_sent = []
    pending_received = []
    _user_friends = []
    for relationship in _user_relationships:
        if relationship.is_pending == 1:
            if relationship.id_user == _user_id:
                pending_sent.append( User.query.filter_by(id=relationship.id_friend).first())
            elif relationship.id_friend == _user_id:
                pending_received.append( User.query.filter_by(id=relationship.id_user).first())
        else:
            _user_friends.append( User.query.filter_by(id=relationship.id_friend).first())
        
        #if relationship.id_user == _user_id:
        #    if relationship.is_pending == 1:
        #        pending_sent.append( User.query.filter_by(id=relationship.id_friend).first())
    #
        #elif relationship.id_friend == _user_id:
        #    if relationship.is_pending == 1:
        #        pending_received.append( User.query.filter_by(id=relationship.id_user).first())
        #else:
        #    _user_friends.append(User.query.filter_by(id=relationship.id_user).first())

    #for relationship in _user_relationships:
    #    if relationship.id_user == _user_id:
    #        _user_friends.append(User.query.filter_by(id=relationship.id_friend).first())
    #    else:
    #        _user_friends.append(User.query.filter_by(id=relationship.id_user).first())
    
    # get user_color_hex for each friend     
    for friend in _user_friends:
        friend.user_color_hex = User_Profile.query.filter_by(id_user=friend.id).first().user_color_hex
    
    # get _user's User_profile hex color
    _user_profile_hex_color = User_Profile.query.filter(User_Profile.id_user == session['id_user']).first().user_color_hex
    return render_template('this_user_profile.html', friend_sent=pending_sent, 
                                                     friend_recieved=pending_received, 
                                                     friends=_user_friends, 
                                                     profile_color = _user_profile_hex_color)


@views.route('/my-profile/change-visibility', methods=['GET', 'POST'])
@login_required
def change_visibility():
    _user_id = session['id_user']
    _user_profile = User_Profile.query.filter_by(id_user=_user_id).first()
    _user_profile.profile_visibility = request.form.get('visibility')
    db.session.add(_user_profile)
    db.session.commit()
    return redirect(url_for('views.my_profile'))

# user profile by username
@views.route('/profile/add-friend', methods=['GET', 'POST'])
@login_required
def get_users():
    if request.method == 'POST':
        _entered_search = request.form.get('search-term').strip()
        _user = User.query.filter((User.email == _entered_search) | 
                                  (User.username == _entered_search)).first()
        
        current_user_id = session['id_user']
        if _user:
            if not _user.id == current_user.id:                                          
                found_useer_id = _user.id
                _user_relationship = User_Relationship(id_user=current_user_id, id_friend=found_useer_id)
                if User_Relationship.query.filter(User_Relationship.id_user == current_user_id, User_Relationship.id_friend == found_useer_id).first():
                    flash('You are already friends with this user.', category='warning')
                    return redirect(url_for('views.my_profile'))
                db.session.add(_user_relationship)
                db.session.commit()
                flash('Friend added.', category='success')
            else:
                flash('You cannot add yourself as a friend.', category='warning')
        else:
            flash('The user does not exist.', category='error')
        
        return redirect(url_for('views.my_profile'))
    
@views.route('/my-profile/delete-friend', methods=['GET', 'POST'])
@login_required
def delete_friend():
    _user_id = session['id_user']
    _friend_id = request.form.get('id_friend')
    print('d----------------------------------------------------')
    print(_user_id, end='\n')
    print(_friend_id)

    _user_relationship = User_Relationship.query.filter(
        (User_Relationship.id_user == _user_id)   & (User_Relationship.id_friend == _friend_id) | 
        (User_Relationship.id_user == _friend_id) & (User_Relationship.id_friend == _user_id)).first() 
    
    print(_user_relationship.id)
    if _user_relationship:
        db.session.delete(_user_relationship)
        db.session.commit()
        flash('Friend deleted.', category='success')
    else:
        flash('Big oops.', category='error')
    return redirect(url_for('views.my_profile'))



@views.route('/profile/<got_user_id>')
@login_required
def profile_page(got_user_id):
    this_user_id = session['id_user']
    
    user_relationship = User_Relationship.query.filter(    
        (User_Relationship.id_user == this_user_id)   & (User_Relationship.id_friend == got_user_id) | 
        (User_Relationship.id_user == got_user_id) & (User_Relationship.id_friend == this_user_id)).first() 
    
    if user_relationship:
        _user_profile = User.query.filter_by(id=got_user_id).first()
        _user_profile.color = User_Profile.query.filter_by(id_user=got_user_id).first().user_color_hex
        return render_template('user_profile.html', user=_user_profile)
    else:
        flash('Big oops', category='error')
        
        
