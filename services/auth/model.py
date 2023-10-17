from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    city = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    birth = db.Column(db.Date)


class Doctor(UserMixin, db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    code = db.Column(db.String(100))
    rate = db.Column(db.Float)
    expertises = db.Column(db.String(100), nullable=False)
    clinic = db.Column(db.String(100))
    image_src = db.Column(db.String(100))
