# Flask-Authentication-System
The Flask Authentication System provides a solid foundation for implementing user authentication and authorization in a Flask application. It follows best practices and includes essential features such as user registration, login, password hashing, and role-based access control. With the suggested improvements and future features, this system can be extended to meet the specific requirements of various applications.


## The file structure of the project looks like this:

    Flask-Authentication-System
    |──instance
    |    ├── db.sqlite         # the database
       

    └── project
        ├── __init__.py       # setup the app
        ├── auth.py           # the auth routes for the app
        ├── main.py           # the non-auth routes for the app
        ├── forms.py          # the WebForms
        ├── models.py         # the database models
        └── templates
            ├── base.html     # contains common layout and links
            ├── base.html     # show the admin create user page with role assignment
            ├── index.html    # show the home page
            ├── login.html    # show the login form
            ├── profile.html  # show the profile page
            └── signup.html   # show the user signup form (user role only)

## Installation

### Clone the repository and navigate to the project directory:

    git clone https://github.com/JWebster-Colby/Flask-Authentication-System.git
    cd Flask-Authentication-System

### Create a virtual environment and activate it:

    python3 -m venv auth
    source auth/bin/activate

### Install the required packages:

    pip install flask flask-sqlalchemy flask-login
    or
    pip install -r requirements.txt

## Configuration

1. Open the `config.py` file and set the `SECRET_KEY` variable to a secure random string.

2. Open the `project/__init__.py` file and update the `SQLALCHEMY_DATABASE_URI` variable if you want to use a different database.

## Usage

Set the FLASK_APP and FLASK_DEBUG environment variables:

    export FLASK_APP=project
    export FLASK_DEBUG=1

Run the Flask application:

    flask run

Open your browser and navigate to [http://localhost:5000/](http://localhost:5000/) to access the application.

## Features
The current features of the Flask Authentication System include:

1. User registration
2. User login
3. Password hashing with bcrypt
4. User roles (admin and user)
5. Profile page displaying user's name and role
6. Creation of new users (admin-only)
7. CSRF protection with Flask-WTF
8. Integration with SQLite database
9. Proper project structure following best practices
10. User authentication with Flask-Login
11. Secure route protection with `@login_required`

## Next Steps

Here are some possible improvements or additional features you can consider for this authentication system:

- Implement additional password complexity requirements.

- Add email confirmation functionality to verify user email addresses before allowing them to register.


- Add a password reset option, allowing users to reset their password if they have forgotten it.

- Implement two-factor authentication (2FA) for an additional layer of security.

- Write unit tests and integration tests to ensure the system functions correctly.

- Implement logging to capture crucial user steps and system events for debugging and monitoring purposes.

- Optimize database queries using techniques like SQLAlchemy's query optimization and database indexing.

- Implement HTTPS and secure HTTP headers to protect data transmission and prevent security vulnerabilities.

- Use more user-friendly URLs to improve the usability and user experience of the application.

- Use a separate file for database configurations to keep the codebase organized.

- Replace passing the `name` parameter to the `profile` page with `current_user.name`.

## Contributors

This project was created by [JWebster-Colby](https://github.com/JWebster-Colby).