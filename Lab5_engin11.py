import sys
import random
import time
import csv

import board
import busio 
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
from datetime import datetime
reset_pin = None
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data...")
print(sys.argv)

start_time = time.time()
run_time = 30
run_time = int(sys.argv[1])
now = start_time 

filename = "time_data.csv"
filename = sys.argv[2]
file = open("combined_data.csv","w",newline='')
dwriter = csv.writer(file)

meta_data = ["Time", "PM10","PM25","PM100"]
dwriter.writerow(meta_data)
print(meta_data)

while (now-start_time) < run_time:
    time.sleep(1)
    now = time.time()
    
    try:
        aqdata = pm25.read()
        datalist = [now,data]
        dwriter.writerow(datalist)
        data = [now,aqdata["pm25 standard"],aqdata["pm100 standard"]]
        data_writer.writerow(data)
        print(data)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
  
file.close()
