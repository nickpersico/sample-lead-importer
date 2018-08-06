from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

from app import routes, models, errors