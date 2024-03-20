import RPi.GPIO as GPIO
import datetime
import time
import sys 
import select 

counts = 0 
def my_callback(channel):
    global counts
    if GPIO.input(channel) == GPIO.HIGH:
        print('\n▼  at ' + str(datetime.datetime.now()))
        counts = counts + 1 
    else:
        print('\n ▲ at ' + str(datetime.datetime.now())) 

#def input_available(timeout):
    # Check if input is available within the specified timeout
    #start_time = time.time()
    # while time.time() - start_time < timeout:
    #run_time = int(sys.argv[1])
    #while time.time() - start_time < run_time:
       # if sys.stdin in select.select([sys.stdin], [], [], timeout)[0]:
          #  return True
    #return False

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback)

    timeout = 10  # 2 minutes in seconds
    start_time = time.time()
    run_time = int(sys.argv[1])

    while time.time() - start_time < run_time:
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            break

        # Check for user input to exit
        # if input_available(0.1):
            # break

        # Add a small delay to reduce CPU usage
        time.sleep(10)
        print(counts,"counts read")
    
 
finally:
    GPIO.cleanup()
# print(counts,"counts read")
print("press enter to exit")
input()
 
print("Goodbye!")
