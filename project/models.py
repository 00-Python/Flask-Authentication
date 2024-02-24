from flask_login import UserMixin
from . import db

# Define the association table for the many-to-many relationship between Users and Roles
# This needs to be done before the User and Role models that reference it
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE')),
    db.Column('role_id', db.Integer, db.ForeignKey('user_role.id', ondelete='CASCADE'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(50))
    roles = db.relationship('UserRole', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True, name='id')
    name = db.Column(db.String(50), unique=True)