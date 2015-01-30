from app import app, db
from app.projects.uploads.models import Sound
import os
import shutil
from flask import g
from flask.ext.login import current_user


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    sounds = db.relationship("Sound", backref="project", lazy="dynamic")

    def __init__(self, project_name):
        self.project_name = project_name
        self.user_id = g.user.id

    def delete_directory(self):
        shutil.rmtree(self.project_directory)
