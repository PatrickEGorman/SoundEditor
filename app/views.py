from app import app, db, login_manager
from app.models import User
from app.projects.models import Project
from flask import render_template, request, flash, redirect, g, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).first()

@app.before_request
def before_request():
    if current_user.is_authenticated():
        g.user = current_user
    else:
        g.user = None

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                login_user(user)
                flash("Login successful!")
                app.config["USER_UPLOAD_FOLDER"] = current_user.user_directory
            else:
                flash("Invalid login. Please try again")
        else:
            flash("Invalid login. Please try again")
        return redirect("/home")
    if not g.user:
        return render_template("home.html")
    else:
        return redirect("/userhome")


@login_required
@app.route("/userhome", methods=["GET", "POST"])
def userhome():
    if request.method == "POST":
        if request.form["create"]:
            if not g.user.projects.filter_by(id=5).first():
                project_name = request.form["project_name"]
                if not Project.query.filter_by(project_name=project_name).first():
                    new_project = Project(project_name=project_name)
                    db.session.add(new_project)
                    db.session.commit()
                    flash("Project created!")
                    return redirect(url_for("project_home", project_id=new_project.id))
                else:
                    flash("Project name already exists!")
                    return redirect("/userhome")
            else:
                flash("Max project limit reached")
                return redirect("/userhome")
    projects = g.user.projects.all()
    return render_template("userhome.html", projects=projects)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect("/home")


@app.route('/create_account', methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        name = request.form["name"]
        user1 = User(username, password, email, name)
        db.session.add(user1)
        db.session.commit()
        return redirect("/home")
    return render_template("create_user.html")


@login_required
@app.route('/delete_account')
def delete_account():
    db.session.delete(current_user)
    db.session.commit()
    return redirect("/home")