from flask import Flask
from flask import Blueprint,render_template

views = Blueprint('views', __name__)


@views.route("/student")
def student():
    return render_template("student.html")


@views.route("/admin",methods=['GET','POST'])
def admin():
    return render_template("admin.html")