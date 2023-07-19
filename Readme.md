# [Student Mark Management System](http://botinterpreters.pythonanywhere.com/)

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
![1](https://github.com/Rajkumar0819/StudentManagement/assets/113299030/c0acea47-9207-434a-b47b-200d67768248)


### As a student:

1. Sign up for an account using the registration form.
2. Log in with your credentials.
3. View your marks and visualize them on the graph.

#### SCREENSHOT 1:
![2](https://github.com/Rajkumar0819/StudentManagement/assets/113299030/bebe249a-59cb-456b-8211-e5bd8cea00dc)


### As an admin:

1. Log in with the admin account.
2. Insert, update, or delete marks from the database.

#### SCREENSHOT 1:
![3](https://github.com/Rajkumar0819/StudentManagement/assets/113299030/d155e591-976b-4d0c-9a10-b177ae5570f2)


#### SCREENSHOT 2
![4](https://github.com/Rajkumar0819/StudentManagement/assets/113299030/5b79d8d8-d33b-49f2-89c0-9b73ee39e780)
