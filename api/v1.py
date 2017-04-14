#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

from flask import request
from flask_restful import Resource
from rasp.light import Light


class NomiWifiLampAPI(Resource):
    def __init__(self):
        self.light = Light(pin=7)

    def get(self):
        return {}, 405

    def put(self, lamp_switch):
        if lamp_switch == "on":
            self.light.turn_on()
            return {"status": "ligada"}, 200
        else:
            self.light.turn_off()
            return {"status": "desligada"}, 200

    def post(self):
        return {}, 405
