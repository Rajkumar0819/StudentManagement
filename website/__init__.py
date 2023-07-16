from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import flask_login

db = SQLAlchemy()

BASE_DIR = path.dirname(path.abspath(__file__))
DB_PATH = path.join(BASE_DIR, "database.db")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "STUDENT MANAGEMENT APPLICATION"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"

    db.init_app(app)

    from .model import User, Marks
    from .views import views 
    from .auth import auth
    
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    create_database(app)
    return app

def create_database(app):
    if not path.exists(DB_PATH):
        with app.app_context():
            db.create_all()