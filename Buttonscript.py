#!/usr/bin/python
#          Uses GPIO5  (BOARD Pin 29)


import RPi.GPIO as gpio
from subprocess import call
import time
import os

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.add_event_detect(5, gpio.FALLING, os.system("ping 8.8.8.8 -c 5"), bouncetime=300)


exit()
