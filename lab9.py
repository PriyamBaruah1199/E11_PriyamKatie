import RPi.GPIO as GPIO
import datetime
import time
import sys 
import select 

meta_data = ["Counts","Time Stamp"]
dwriter.writerow(meta_data)
print(meta_data)

counts = 0 
def my_callback(channel):
    global counts
    print('\n▼  at ' + str(datetime.datetime.now()))
    counts = counts + 1 

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback)
 
start_time = time.time()
run_time = int(sys.argv[1])
filename = sys.argv[2]

while time.time() - start_time < run_time:
    time.sleep(10)
    print(counts,"counts read")
    data = [counts]
        dwriter.writerow(data)
    counts = 0
    


