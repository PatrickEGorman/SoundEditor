__author__ = 'patrickgorman'
from app import db


class Sound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __init__(self, filename, project_id):
        self.filename = filename
        self.project_id = project_id