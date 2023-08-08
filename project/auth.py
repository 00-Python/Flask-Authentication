from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # Login Code Goes Here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Chech if user exists, hash provided pass and compare
    if not user or not check_password_hash(user.password, password):
        flash('Please check logindetails and try again!')
        return redirect(url_for('auth.login'))

    # if all checks pass redirect to profile page
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to db goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # check if email already exists in db
    user = User.query.filter_by(email=email).first()

    # if user already exists redirect back to signup page to retry
    if user:
        flash('User already exists!')
        return redirect(url_for('auth.signup'))

    # Create a new user with the data from the form and hash the pass for security
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256')) 

    # Add New User to db
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'
