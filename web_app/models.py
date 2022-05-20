from sysconfig import is_python_build
import uuid

from matplotlib.pyplot import table
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class User_Relationship(db.Model):
    __tablename__ = 'User_Relationship'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_friend = db.Column(db.Integer)
    is_pending = db.Column(db.Boolean, default=True)

class User_Profile(db.Model):
    __tablename__ = 'User_Profile'
    id_user = db.Column(db.String(36), primary_key=True)
    user_color_hex = db.Column(db.String(8), default='#65CC4C')


class Rental_Unit(db.Model):
    __tablename__ = 'Rental_Unit'
    id = db.Column(db.Integer, primary_key=True)
    id_owner = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36), primary_key=True)
    address = db.Column(db.String(120), primary_key=True)


class Rental_Unit_Payment(db.Model):
    __tablename__ = 'Rental_Unit_Payment'
    id = db.Column(db.Integer, primary_key=True)
    id_rental_unit = db.Column(db.Integer, primary_key=True)
    id_payment_history = db.Column(db.String(36), primary_key=True)
    monthly_due = db.Column(db.Integer, primary_key=True)


class Payment_History(db.Model):
    __tablename__ = 'Payment_History'
    id = db.Column(db.Integer, primary_key=True)
    payment_date = db.Column(db.DateTime, primary_key=True)
