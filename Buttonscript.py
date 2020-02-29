#!/usr/bin/python
#     Pin 10 is input and initial value is low (OFF)


import RPi.GPIO as GPIO
import os


def button_callback(channel):
    print("Starting Update!")
    os.system ("ping 8.8.8.8 -C 5")

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)



exit()
