# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from flask import Flask, g
from .db import DB


def create_app():
    """Basic project app."""

    # app config
    app = Flask(__name__, instance_relative_config=True)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '123'
    app.config['MYSQL_DB'] = 'car_hiring'

    db = DB(app.config['MYSQL_HOST'], app.config['MYSQL_USER'], app.config['MYSQL_DB'], app.config['MYSQL_PASSWORD'])
    # app.db = db.mysqlconnect()

    @app.before_request
    def before_request():
        g.db = db.mysqlconnect()

    # user api blueprint
    from .user.user_api import user_api
    app.register_blueprint(user_api)

    return app
