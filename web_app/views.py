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
    # gets user's friends from User_Relationship where 
    # id_user or id_friend is equal to session['id_user
    _user_id = session['id_user']

    _user_relationships = User_Relationship.query.filter((User_Relationship.id_user == _user_id) | (User_Relationship.id_friend == _user_id)).all()
    
    _user_friends = []    
    for relationship in _user_relationships:
        if relationship.id_user == _user_id:
            _user_friends.append(User.query.filter_by(id=relationship.id_friend).first())
        else:
            _user_friends.append(User.query.filter_by(id=relationship.id_user).first())
            
    for friend in _user_friends:
        _user_profile = User_Profile.query.filter_by(id_user=friend.id).first()
        friend.user_color_hex = _user_profile.user_color_hex
    # get user's User_profile hex color
    _user_profile = User_Profile.query.filter(User_Profile.id_user == session['id_user']).first()
    _user_profile_hex_color = _user_profile.user_color_hex
    return render_template('this_user_profile.html', friends = _user_friends, profile_color = _user_profile_hex_color)

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