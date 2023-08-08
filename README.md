# Flask-Login Authentication App
credit: `https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login`

This project demonstrates how to add authentication to a Flask app with Flask-Login. It allows users to log in and access protected pages, and displays information from the user's account on their profile page.

## Project Structure

The file structure of the project looks like this:

```
flask_auth_app
└── project
    ├── __init__.py       # setup the app
    ├── auth.py           # the auth routes for the app
    ├── db.sqlite         # the database
    ├── main.py           # the non-auth routes for the app
    ├── models.py         # the user model
    └── templates
        ├── base.html     # contains common layout and links
        ├── index.html    # show the home page
        ├── login.html    # show the login form
        ├── profile.html  # show the profile page
        └── signup.html   # show the signup form
```

## Installation

1. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/username/flask_auth_app.git
cd flask_auth_app
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv auth
source auth/bin/activate
```

3. Install the required packages:

```bash
pip install flask flask-sqlalchemy flask-login
```

## Usage

1. Set the FLASK_APP and FLASK_DEBUG environment variables:

```bash
export FLASK_APP=project
export FLASK_DEBUG=1
```

2. Run the Flask application:

```bash
flask run
```

3. Open a web browser and navigate to `localhost:5000` to access the app.

