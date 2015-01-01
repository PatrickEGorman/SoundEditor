import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = "postgres://patrickgorman:soundeditor@localhost:5432/patrickgorman"
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = "Sound_editor"
UPLOAD_FOLDER = '/Users/patrickgorman/documents/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}
app.config['STATIC_FOLDER'] = 'static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key=SECRET_KEY