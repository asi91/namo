from .app import app, logger
from flask import render_template, request


@app.route("/")
def index():
    # logger.info(request.headers.get("User-Agent"))
    logger.info(request.user_agent.browser)
    return render_template("index.html")
