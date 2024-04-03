import RPi.GPIO as GPIO
import datetime
import time
import sys
import select
import csv

meta_data = ["Counts", "Time Stamp"]

# Open a CSV file for writing
with open(sys.argv[2], 'w', newline='') as csvfile:
    dwriter = csv.writer(csvfile)

    # Write the metadata to the CSV file
    dwriter.writerow(meta_data)
    print(meta_data)

    counts = 0

    def my_callback(channel):
        global counts
        print('\n▼  at ' + str(datetime.datetime.now()))
        counts += 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback)

    start_time = time.time()
    run_time = int(sys.argv[1])

    while time.time() - start_time < run_time:
        time.sleep(10)
        print(counts, "counts read")
        
        # Write the counts and timestamp to the CSV file
        data = [counts, str(datetime.datetime.now())]
        dwriter.writerow(data)
        counts = 0

print("Data writing complete.")
