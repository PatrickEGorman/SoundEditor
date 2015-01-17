import os
from flask import request, redirect, url_for, flash, send_from_directory
from flask.ext.login import login_required
from werkzeug.utils import secure_filename
from app import app, db
from app.projects.models import Project
from models import Sound

def allowed_filename(filename):
    return "." in filename and \
        filename.split(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]

@login_required
@app.route("/add_file/<project_id>", methods=["GET", "POST"])
def file_upload(project_id):
    file = request.files['file']
    if file and allowed_filename(file.filename):
        filename = secure_filename(file.filename)
        directory = Project.query.filter_by(id=project_id).first().project_directory
        file.save(os.path.join(directory, filename))
        sound = Sound(filename, project_id)
        db.session.add(sound)
        db.session.commit()
        return redirect(url_for('uploaded_file', filename=filename, project_id=project_id))


@login_required
@app.route('/uploads/<filename>/<project_id>')
def uploaded_file(filename, project_id):
    directory = Project.query.filter_by(id=project_id).first().project_directory
    return send_from_directory(directory=directory,
                               filename=filename)

@login_required
@app.route('/delete')
def none_selected():
    flash("No Sounds Selected!")
    return redirect('url')


@login_required
@app.route('/delete/<delete_string>')
def delete_sounds(delete_string):
    strings = delete_string.split('d')
    project_id = strings[0]
    project = Project.query.filter_by(id=project_id).first()
    for sound_id in strings[1:]:
        sound = project.sounds[int(sound_id)]
        db.session.delete(sound)
    db.session.commit()
    return redirect(
        url_for("project_home",
                project_name=project.project_name)
    )