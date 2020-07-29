from flask import Flask
from .log_handler import rotate_log_by_minute

app = Flask(__name__)
logger = rotate_log_by_minute()

from . import routes
