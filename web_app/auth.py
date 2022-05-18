import re

from flask_login import LoginManager, login_user, login_required, logout_user, login_manager, login_required, current_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/auth', methods=['GET', 'POST'])
def auth_user():
    data = request.form
    auth_type = request.args.get('auth_type')
    l_email = request.args.get('l_email')
    print(auth_type)

    errors_list = []
    if request.method == 'POST':
        if auth_type == 'login':
            l_username_or_email = request.form.get('l_email').strip()
            l_password = request.form.get('l_password').strip()

            # if empty
            errors = False
            if l_username_or_email == '' or l_password == '':
                flash('Please fill all fields', category='error')
                return redirect('/auth?auth_type=login')

            user = User.query.filter((User.email == l_username_or_email) | (
                User.username == l_username_or_email)).first()

            if user:
                print(user.password)
                if not check_password_hash(user.password, l_password):
                    errors = True
            else:
                errors = True

            if not errors:
                flash('SUccesfull login', category='success')
                login_user(user)
                session['id_user'] = user.id
                return redirect(url_for('views.dash'))
            else:
                flash('Username/email or password is incorrect', category='error')
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
                flash("Fill all fields", category='error')

            _user = User.query.filter_by(email=r_email).first()
            if _user:
                flash('User already exist', category='error')
                errors = True

            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', r_email):
                flash('Please enter valid email', category='error')
                errors = True

            if not r_password == r_verify_password:
                flash('Passwords do not match', category='error')
                errors = True

            # hash password
            if not errors:
                r_password = generate_password_hash(
                    r_password, method='sha256')
                new_user = User(username=r_username,
                                email=r_email, password=r_password)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                redirect(url_for('views.dash'))
                flash(f'You are registered {r_username}', category='success')

    return render_template('auth.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', category='success')
    return redirect(url_for('auth.auth_user'))
