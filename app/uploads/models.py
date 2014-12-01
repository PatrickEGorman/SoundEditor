from app import db


class Sound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String)

    def __init__(self, file_name):
        self.file_name = file_name