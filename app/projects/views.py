__author__ = 'patrickgorman'
import os
from app import app, db
from flask import render_template, request, flash, redirect, url_for, g
from models import Project
from app.projects.uploads.models import Sound
from flask.ext.login import login_required
from werkzeug.utils import secure_filename



def allowed_filename(filename):
    return "." in filename and \
        filename.split(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]

@login_required
@app.route("/project/<project_name>", methods=["GET", "POST"])
def project_home(project_name):
    project = Project.query.filter_by(project_name=project_name).first()
    if request.method == "POST":
        pass
    return render_template("projects/project.html", project=project)


@login_required
@app.route("/remove/<project_id>")
def remove(project_id):
    project = Project.query.filter_by(id=project_id).first()
    for sound in project.sounds:
        db.session.delete(sound)
    project.delete_directory()
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted!")
    return redirect("/userhome")