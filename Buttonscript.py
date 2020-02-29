#!/usr/bin/python
#     Pin 10 runs script
#     Pin 11 runs exit command
#     Script should wait for 500seconds


import RPi.GPIO as GPIO
import os
import time

def run(channel):
    print("Starting Update!")
    os.system ("ping 8.8.8.8 -C 5")

def exit(channel):
    print("About to Exit!")
    os.system ("exit")

def WAIT():
    time.sleep(500)

GPIO.setwarnings (False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=run)
GPIO.add_event_detect(11,GPIO.RISING,callback=exit)



WAIT()
