import RPi.GPIO as GPIO
import datetime

count= 0 
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
        count = count + 1
        print(count)
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback)
    
    message = input('\nPress Enter to exit.\n')

 
finally:
    GPIO.cleanup()
 
print("Goodbye!")
