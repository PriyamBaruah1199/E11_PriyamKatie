import RPi.GPIO as GPIO
import datetime
import time

def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback)

    timeout = 20  # 2 minutes in seconds
    start_time = time.time()

    while True:
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            break

        # Check for user input to exit
        if input_available():
            break

        # Add a small delay to reduce CPU usage
        time.sleep(0.1)
    
    
    message = input('\nPress Enter to exit.\n')

 
finally:
    GPIO.cleanup()
 
print("Goodbye!")
