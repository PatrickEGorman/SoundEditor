import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = "Sound_editor"
UPLOAD_FOLDER = '/Users/patrickgorman/pycharmprojects/soundeditor/app/templates/uploads/audio'
OPEN_FOLDER = 'templates/uploads/audio'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app.config['OPEN_FOLDER'] = OPEN_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key=SECRET_KEY