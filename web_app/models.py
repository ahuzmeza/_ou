import uuid

from matplotlib.pyplot import table
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class User_Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.String(36), db.ForeignKey('user.id'))
    id_friend = db.Column(db.String(36), db.ForeignKey('id_friend.id'))


class User_Profile(db.Model):
    id_user = db.Column(db.String(36), primary_key=True)
    #image = db.Column(db.Blob())
    set_theme = db.Column(db.String(80), default='default_theme')


class Rental_Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_owner = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), primary_key=True)
    address = db.Column(db.String(120), primary_key=True)


class Rental_Unit_Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_rental_unit = db.Column(db.Integer, primary_key=True)
    id_payment_history = db.Column(db.String(36), primary_key=True)
    monthly_due = db.Column(db.Integer, primary_key=True)


class Payment_History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_date = db.Column(db.DateTime, primary_key=True)
