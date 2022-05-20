import random
import re

from flask_login import LoginManager, login_user, login_required, logout_user, login_manager, login_required, current_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from .models import User, User_Profile
from PIL import ImageColor


auth = Blueprint('auth', __name__)


@auth.route('/auth', methods=['GET', 'POST'])
def auth_user():
    data = request.form
    auth_type = request.args.get('auth_type')
    l_email = request.args.get('l_email')
    cb_remember_me = request.form.get('cb_keep_signed_in')

    print(auth_type)
    # do something

    errors_list = []
    if request.method == 'POST':
        if auth_type == 'login':
            l_username_or_email = request.form.get('l_email').strip()
            l_password = request.form.get('l_password').strip()
            remember_me = 'cb_remember_me' in request.form
            
            errors = False
            if l_username_or_email == '' or l_password == '':
                flash('Please fill all fields', category='error')
                return redirect('/auth?auth_type=login')

            user = User.query.filter((User.email == l_username_or_email) | (
                User.username == l_username_or_email)).first()

            if user:
                if not check_password_hash(user.password, l_password):
                    errors = True
            else:
                errors = True

            if not errors:
                flash('SUccesfull login.', category='success')
                login_user(user)
                session.permanent = remember_me
                session['id_user'] = user.id
                return redirect(url_for('views.dash'))
            else:
                flash('User details incorrect.', category='error')
                redirect('/auth?auth_type=login')

        if auth_type == 'register':
            r_username = request.form.get('r_username')
            r_email = request.form.get('r_email')
            r_password = request.form.get('r_password')
            r_verify_password = request.form.get('r_verify_password')

            errors = False
            _form = request.form
            for key in _form.keys():
                for value in _form.getlist(key):
                    if request.form.get(key) == '':
                        errors = True
            if errors:
                flash("All fields required", category='error')
                return redirect('/auth?auth_type=register')

            if ' ' in r_username:
                flash('Username cannot contain spaces.', category='error')
                return redirect('/auth?auth_type=register')

            _user = User.query.filter_by(email=r_email).first()
            if _user:
                flash('User already exists.', category='error')
                errors = True

            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', r_email):
                flash('Invalid email.', category='error')
                errors = True

            if not r_password == r_verify_password:
                flash('Passwords do not match.', category='error')
                errors = True

            # hash password
            if not errors:
                r_password = generate_password_hash(
                    r_password, method='sha256')                
                new_user = User(username=r_username,
                                email=r_email, password=r_password)
                db.session.add(new_user)

                login_user(new_user)
                created_user = db.session.query(User).filter_by(email=r_email).first()
                new_user_id = created_user.id                
                print(new_user_id)
                print("--------------------------------")
                
                # add random color to user profile
                random_color_hex = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                new_user_profile = User_Profile(id_user=new_user_id, user_color_hex=random_color_hex)
                db.session.add(new_user_profile)
                
                db.session.commit()               
               
                redirect(url_for('views.dash'))
                flash(
                    f'You registered succesfully! {r_username}', category='success')

    return render_template('auth.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', category='success')
    return redirect(url_for('auth.auth_user'))
