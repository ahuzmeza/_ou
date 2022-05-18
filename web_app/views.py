from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def dash():
    _user = session['id_user']
    print(current_user.username)
    return render_template('dashboard.html')
