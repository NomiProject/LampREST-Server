#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

from webserver import Webservice

if __name__ == "__main__":
    app = Webservice(__name__, debug=False)
    app.execute()
