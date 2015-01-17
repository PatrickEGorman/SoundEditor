__author__ = 'patrickgorman'
import os
from app import app, db
from flask import render_template, request, flash, redirect
from models import Project
from flask.ext.login import login_required



def allowed_filename(filename):
    return "." in filename and \
        filename.split(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]

@login_required
@app.route("/project/<project_id>", methods=["GET", "POST"])
def project_home(project_id):
    project = Project.query.filter_by(id=project_id).first()
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