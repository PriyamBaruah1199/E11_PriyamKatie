import RPi.GPIO as GPIO
import datetime
import time
import sys 
import select 

counts = 0 
def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 

def input_available(timeout):
    # Check if input is available within the specified timeout
    start_time = time.time()
    while time.time() - start_time < timeout:
        if sys.stdin in select.select([sys.stdin], [], [], timeout)[0]:
            return True
    return False

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback, counts = counts + 1)

    timeout = 10  # 2 minutes in seconds
    start_time = time.time()

    while True:
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            break

        # Check for user input to exit
        if input_available(0.1):
            break

        # Add a small delay to reduce CPU usage
        time.sleep(0.1)
    
 
finally:
    GPIO.cleanup()
print(counts,"counts read")
print("press enter to exit")
input()
 
print("Goodbye!")
