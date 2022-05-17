import re
from flask import Blueprint, render_template, request, flash

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
            if l_email == '' or l_password == '':
                flash('Please fill all fields', category='error')
            
            # input validation
            # --------------------------------
                
        if auth_type == 'register':
            r_username = request.form.get('r_username')
            r_email = request.form.get('r_email')
            r_password = request.form.get('r_password')
            r_verify_password = request.form.get('r_verify_password')
            print(r_username, r_email, r_password, r_verify_password)
            
    return render_template('auth.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"
