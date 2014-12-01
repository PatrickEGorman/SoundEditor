from app import app, db
from app.uploads.models import Sound
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")