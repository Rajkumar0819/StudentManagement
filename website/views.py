from flask import redirect,url_for,request,flash
from flask import Blueprint,render_template
from flask_login import login_required, current_user
from .model import Marks, User
from . import db, DB_PATH
import sqlite3
 
views = Blueprint('views', __name__)


@views.route("/student")
@login_required
def student():
    try :
        marks_list = Marks.query.filter_by(email=current_user.email).first()
        mark_values = [marks_list.mark1, marks_list.mark2, marks_list.mark3, marks_list.mark4, marks_list.mark5]
    except :
        mark_values=[0,0,0,0,0]
    return render_template("student.html",user = current_user,mark_values = mark_values)


@views.route("/admin",methods=['GET','POST'])
@login_required
def admin():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    insert_table_data = c.execute("""SELECT first_name, email FROM user WHERE email NOT IN (SELECT email FROM marks) AND id != (SELECT MIN(id) FROM user)""")
    insert_table_data = insert_table_data.fetchall()


    update_table_data = c.execute("""SELECT email,name,mark1,mark2,mark3,mark4,mark5 FROM marks """)
    update_table_data = update_table_data.fetchall()

    delete_table_data = c.execute("SELECT first_name, email FROM user WHERE id NOT IN (SELECT MIN(id) FROM user)")
    delete_table_data = delete_table_data.fetchall()

    return render_template("admin.html",user = current_user, insert_table_data = insert_table_data,update_table_data = update_table_data,delete_table_data = delete_table_data)


@views.route("/insert",methods=['POST'])
@login_required
def insert_data():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        mark1 = request.form.get("mark1")
        mark2 = request.form.get("mark2")
        mark3 = request.form.get("mark3")
        mark4 = request.form.get("mark4")
        mark5 = request.form.get("mark5")
        value = Marks(email = email,name = name,mark1=mark1,mark2=mark2,mark3=mark3,mark4=mark4,mark5=mark5)
        db.session.add(value)
        db.session.commit()
    return redirect(url_for("views.admin"))


@views.route("/update",methods=['POST'])
@login_required
def update_data():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        mark_select = request.form.get('markSelect')
        mark_value = request.form.get('markValue')
        marks = Marks.query.filter_by(email=email).first()

    # Update the record with new values
        if mark_select == 'mark1':
            marks.mark1 = mark_value
        elif mark_select == 'mark2':
            marks.mark2 = mark_value
        elif mark_select == 'mark3':
            marks.mark3 = mark_value
        elif mark_select == 'mark4':
            marks.mark4 = mark_value
        elif mark_select == 'mark5':
            marks.mark5 = mark_value

        # Commit the changes to the database
        db.session.commit()

        flash("data is Updated successfuly",category="success")
        return redirect(url_for("views.admin"))


@views.route("/delete",methods=['POST'])
@login_required
def delete_data():
    if request.method == "POST":
        email = request.form.get('email')

        # Retrieve the user to delete from the database
        user = User.query.filter_by(email=email).first()
        user_marks = Marks.query.filter_by(email=email).first()

        # Check if the user exists
        if user:
            # Delete the user
            db.session.delete(user)
            db.session.commit()
        if user_marks:
            # Delete the user
            db.session.delete(user_marks)
            db.session.commit()
    return redirect(url_for("views.admin"))