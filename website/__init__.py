from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sqlite3

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
    admin()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" 
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return User.query.get(email)

    return app

def create_database(app):
    if not path.exists(DB_PATH):
        with app.app_context():
            db.create_all()


def admin():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Execute the INSERT query
    c.execute("INSERT OR IGNORE INTO User (email, password, first_name, role) VALUES ('admin@gmail.com', 'admin123', 'Admin', 'admin')")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()