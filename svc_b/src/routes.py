from .app import app
from flask import render_template
from .log_grab import ACCESS_STATS


@app.route("/")
def index():
    return render_template("index.html", data=ACCESS_STATS)
