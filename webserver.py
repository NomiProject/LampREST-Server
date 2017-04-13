#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

from flask import Flask, render_template, jsonify
from flask import make_response
from flask_restful import Api
from werkzeug.contrib.cache import SimpleCache
from api.v1 import NomiWifiLampAPI


class Webservice(Flask):
    def __init__(self, name, host='0.0.0.0', port=5000, debug=True):
        Flask.__init__(self, name)
        self.host = host
        self.port = port
        self.debug = debug
        self.cache = SimpleCache()
        self.api = Api(self, catch_all_404s=True, errors={
            'BadRequest': {
                'message': 'Your request is not invalid',
                'status': 400
            },
            'Unauthorized': {
                'message': 'Unauthorized access, please verify your credentials',
                'status': 401
            },
            'Forbidden': {
                'message': 'Unauthorized access, please verify if you have authorization to access this content',
                'status': 403
            },
            'NotFound': {
                'message': 'Could not find it',
                'status': 404
            },
            'MethodNotAllowed': {
                'message': 'Method not allowed or invalid',
                'status': 405
            },
            'InternalServerError': {
                'message': 'Internal Error. Please, contact the system administrator',
                'status': 500
            }
        })

    def __load_page(self, page):
        page_name = page.split(".")[0]
        response = self.cache.get(page_name + "_page")
        if response is None:
            response = render_template(page)
            self.cache.set(page_name + "page", response, timeout=5 * 60)
        return response

    def pages(self):
        @self.route("/")
        def main():
            return self.__load_page("home.html")

    def execute(self):
        self.pages()
        self.api.add_resource(NomiWifiLampAPI, '/api/v1.0/wifi/lamp/<string:lamp_switch>')
        self.run(self.host, self.port, self.debug)
