# Student Mark Management System

This is a web-based application built with Flask that allows students to create accounts, view their marks, and for administrators to insert, update, and delete marks in the database.

## Features

- User Registration: Students can sign up for an account by providing their credentials, such as username, password, and any other necessary information.

- User Authentication: Once registered, students can log in to the system using their credentials. Flask-Login handles the authentication process and manages user sessions.

- Mark Management: Administrators have the ability to insert, update, and delete marks in the database. This allows them to manage the marks of students effectively.

- Marks Visualization: Students can view their marks in the form of a graph, which provides a visual representation of their performance over time. This feature helps students track their progress and identify trends.

## Technologies Used

- Flask: Flask is a Python web framework used to build the application. It provides a simple and flexible way to develop web applications.

- Flask-Login: Flask-Login is a Flask extension that handles user authentication and session management. It simplifies the process of managing user login sessions.

- SQLAlchemy: SQLAlchemy is an Object-Relational Mapping (ORM) library used to interact with the SQLite database. It provides an abstraction layer to perform database operations using Python code.

- SQLite: SQLite is a lightweight, file-based database management system. It is used to store student information and marks in this application.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/student-mark-management.git
```

2. Create a Virtual Environment (Optional)
```
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```
4. Run the Program
```
py main.py
```

## Usage

### As a student:

1. Sign up for an account using the registration form.
2. Log in with your credentials.
3. View your marks and visualize them on the graph.

#### SCREENSHOT 1:

### As an admin:

1. Log in with the admin account.
2. Insert, update, or delete marks from the database.

#### SCREENSHOT 1:
#### SCREENSHOT 2: