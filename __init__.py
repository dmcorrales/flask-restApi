from flask import Flask, Blueprint
import os
from .extensions import db, ma
from .controller import main


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.run(debug=True)
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(main)
    return app

