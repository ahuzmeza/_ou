from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def dash():
   return render_template('dashboard.html')