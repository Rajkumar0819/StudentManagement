from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), db.ForeignKey('user.email'))
    mark1 = db.Column(db.Integer)
    mark2 = db.Column(db.Integer)
    mark3 = db.Column(db.Integer)
    mark4 = db.Column(db.Integer)
    mark5 = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    


class User(db.Model, UserMixin):
    email = db.Column(db.String(150), unique=True,primary_key=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    marks = db.relationship('Marks')