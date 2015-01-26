import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = "postgres://patrickgorman:soundeditor@localhost:5432/patrickgorman"
    UPLOAD_FOLDER = '/Users/patrickgorman/documents/uploads'
    SECRET_KEY = "Sound_editor"
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    UPLOAD_FOLDER = os.environ['TRANSLOADIT_URL']
    SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_EXTENSIONS = {'mp3', 'wav'}
app.config['STATIC_FOLDER'] = 'static'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY
