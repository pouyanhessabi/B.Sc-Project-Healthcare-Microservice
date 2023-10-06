from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserDisease(db.Model):
    __tablename__ = "user_disease"
    user_id = db.Column(db.Integer, primary_key=True)
    disease = db.Column(db.String(100), primary_key=True)
    ratio = db.Column(db.Float)
    req_date = db.Column(db.Date, primary_key=True)


class UserExpertise(db.Model):
    __tablename__ = "user_expertise"
    user_id = db.Column(db.Integer, primary_key=True)
    expertise = db.Column(db.String(100), primary_key=True)
    ratio = db.Column(db.Float)
    req_date = db.Column(db.Date, primary_key=True)
