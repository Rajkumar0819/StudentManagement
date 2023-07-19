from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route("/signup",methods=["GET",'POST'])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email = email).first()
        if email == "admin@gmail.com":
            flash("This is a Email for Admin Sign As Student try another email",category="error")
        elif user:
            flash("Email Already exist", category='error')
        elif len(email) < 4:  
            flash("Email must be greater than 4 characters", category="error")
        elif len(first_name) < 2:  
            flash("Name must be at least 4 characters", category="error")
        elif password1 != password2:
            flash("Entered password incorrectly type again", category="error")
        elif len(password1) < 7:  
            flash("password length must be at least 7 characters", category="error")
        else:
            new_user = User(email = email, password = generate_password_hash(password1, method='scrypt'), first_name = first_name)
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created Successfully!!!", category="success")
            login_user(new_user)
            return redirect(url_for('views.student'))
    return render_template("signup.html",user = current_user)


@auth.route("/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if user.email == "admin@gmail.com" and user.password =="admin123":
                flash("Logged in Successfully as Admin", category="success")
                login_user(user)
                return redirect(url_for("views.admin"))

            elif check_password_hash(user.password,password):
                flash("Logged in Successfully", category="success")
                login_user(user)
                return redirect(url_for("views.student"))     
               
    return render_template("login.html", user = current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))