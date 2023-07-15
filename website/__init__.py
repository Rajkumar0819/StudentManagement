from flask import Flask
import sqlite3
import flask_login

def create_app():
    app = Flask(__name__)

    return app