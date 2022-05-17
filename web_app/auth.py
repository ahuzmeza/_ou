from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/auth', methods=['GET', 'POST'])
def login():
    data = request.form
    auth_type = request.args.get('auth_type')
    # true - logn
    # flase - register
    
    errors_list = []
    if request.method == 'POST':
        if auth_type == 'login':
            l_email = request.form.get('l_email').strip()
            l_password = request.form.get('l_password').strip()
            
            # if empty
            errors = False
            if l_email == '' or l_password == '':
                flash('Please fill all fields', category='error')
                errors = True
            
            
            # input validation
            # --------------------------------
                
        if auth_type == 'register':
            r_username = request.form.get('r_username')
            r_email = request.form.get('r_email')
            r_password = request.form.get('r_password')
            r_verify_password = request.form.get('r_verify_password')
            print(r_username, r_email, r_password, r_verify_password)
            
            errors = False
            
            # hash password
            r_password = generate_password_hash(r_password, method='sha256')
            if not errors:
                new_user = User(username=r_username, email=r_email, password=r_password)
                db.session.add(new_user)
                db.session.commit()
                flash(f'You are registered {r_username}', category='success')
                redirect(url_for('auth.login'))
                
    return render_template('auth.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"
