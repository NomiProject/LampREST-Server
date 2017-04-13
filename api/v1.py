#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

from flask import request
from flask_restful import Resource
from werkzeug.useragents import UserAgent


class NomiWifiLampAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        return {}, 405

    def put(self, lamp_switch):
        return ({"status": "123 ligada"}) if lamp_switch == "on" else ({"status": "desligada"})

    def post(self):
        return {}, 405
