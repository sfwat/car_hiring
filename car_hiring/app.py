# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    """Basic project app."""

    # app config
    app = Flask(__name__, instance_relative_config=True)

    # user api blueprint
    from .user.user_api import user_api
    app.register_blueprint(user_api)

    return app
