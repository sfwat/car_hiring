# -*- coding: utf-8 -*-
"""
user api

"""
from flask import jsonify, request as current_request
from ..util.blueprint import AppBlueprint
from .user import Customer


user_api = AppBlueprint('user', __name__)
api = user_api


@api.POST("/customer")
def add_customer():
    payload = current_request.get_json()
    new_customer = Customer(name=payload["username"], email=payload["email"], phone=payload["phone"])
    return new_customer.create()


@api.GET("/customer/<id>")
def get_customer(id):
    customer = Customer(id=id)
    return customer.get()


@api.DELETE("/customer/<id>")
def remove_customer(id):
    customer = Customer(id=id)
    return customer.delete()

