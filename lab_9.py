# -*- coding: utf-8 -*-
"""Lab 9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ya4xER98oDfRzx-SOHry8K6U2QtFwJ_B
"""

# Step 4

import RPi.GPIO as GPIO
import datetime

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')

while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)


GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
do_something()
if GPIO.event_detected(channel):
    print('Button pressed')


def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)

GPIO.remove_event_detect(channel)

