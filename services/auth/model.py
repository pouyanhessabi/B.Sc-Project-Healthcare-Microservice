from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class UserDisease(db.Model):
    __tablename__ = "user_disease"
    user_id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(100), primary_key=True)
    rate = db.Column(db.Float)
    req_date = db.Column(db.Date, primary_key=True)


class UserExpertise(db.Model):
    __tablename__ = "user_expertise"
    user_id = db.Column(db.Integer, primary_key=True)
    expertise = db.Column(db.String(100), primary_key=True)
    rate = db.Column(db.Float)
    req_date = db.Column(db.Date, primary_key=True)
