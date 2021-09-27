# -*- coding: utf-8 -*-
"""
user api

"""
from flask import jsonify, request as current_request
from ..util.blueprint import AppBlueprint


user_api = AppBlueprint('user', __name__)
api = user_api


