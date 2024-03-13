import RPi.GPIO as GPIO
import datetime
 
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 
 
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)

 
finally:
    GPIO.cleanup()

my_callback(1)

print("Goodbye!")
