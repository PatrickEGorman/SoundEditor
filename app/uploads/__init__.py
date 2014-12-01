__author__ = 'patrickgorman'

from app import app
from flask.ext.uploads import UploadSet, AUDIO, configure_uploads

audio = UploadSet('audio', AUDIO, default_dest=lambda application: application.instance_path)
configure_uploads(app, audio)
