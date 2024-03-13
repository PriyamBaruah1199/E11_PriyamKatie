import RPi.GPIO as GPIO
import datetime

GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if GPIO.input(1l):
    print('Input was HIGH')
else:
    print('Input was LOW')

while GPIO.input(1) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

channel = GPIO.wait_for_edge(1, GPIO_RISING, timeout=5000)
if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)

#event detected 
GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
do_something()
if GPIO.event_detected(channel):
    print('Button pressed')

def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)  # add rising edge detection on a channel

