from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    email = db.Column(db.String(150),db.ForeignKey('user.email'))
    name = db.Column(db.String(150))
    mark1 = db.Column(db.Integer)
    mark2 = db.Column(db.Integer)
    mark3 = db.Column(db.Integer)
    mark4 = db.Column(db.Integer)
    mark5 = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    

class User(db.Model, UserMixin):

    # table datas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    role = db.Column(db.String(20), nullable=False, default='student')  

    # realtionship
    marks = db.relationship('Marks', backref='user')
