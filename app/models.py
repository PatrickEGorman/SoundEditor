from app import app, db
from app.projects.models import Project
import os
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    email = db.Column(db.String)
    name = db.Column(db.String)
    projects = db.relationship('Project', backref='user', lazy='dynamic')

    def __init__(self, username, password, email, name):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email
        self.name = name

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)