#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Allex Lima <allexlima@unn.edu.br> | www.allexlima.com

import RPi.GPIO as GPIO


class Light(object):
    def __init__(self, pin=7):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin, True)

    def turn_off(self):
        GPIO.output(self.pin, False)
