from app import app, db
from app.uploads import audio
from app.uploads.models import Sound
import os
from flask import request, render_template, redirect, url_for, abort, flash, send_from_directory
from werkzeug.utils import secure_filename


def allowed_filename(filename):
    return "." in filename and \
        filename.split(".",1)[1] in app.config["ALLOWED_EXTENSIONS"]


@app.route('/uploads/<filename>')
def get_sound(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files['sound']
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            flash("Sound Uploaded!")
            return redirect(url_for('upload_file', filename=filename))
    return render_template("uploads/upload.html")


@app.route('/sound/<filename>')
def upload_file(filename):
    return render_template("uploads/sound.html", sound=filename)

