import sys
import random
import time
import csv
import adafruit_bme680
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
# Create sensor object
i2c = board.I2C() # Uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25 

print("Found PM2.5 sensor, reading data...")
print(sys.argv)


time.sleep(30)

start_time = time.time()
#run_time = 30
run_time = int(sys.argv[1])
now = start_time 

filename = "time_data.csv"
filename = sys.argv[2]
file = open(filename,"w",newline='')
dwriter = csv.writer(file)

meta_data = ["Time", "PM10","PM25","PM100","Temperature","Gas","Relative Humidity","Pressure","Altitude"]
dwriter.writerow(meta_data)
print(meta_data)


while (now-start_time) < run_time:
    time.sleep(1)
    now = time.time()
    
    print(now, " seconds have passed","Temperature: %0.1f C" % bme680.temperature,"Gas: %d ohm" % bme680.gas,"Humidity: %0.1f %%" % bme680.relative_humidity,"Pressure: %0.3f hPa" % bme680.pressure,"Altitude = %0.2f meters" % bme680.altitude)
    
    try:
        aqdata = pm25.read()
        data = [now,aqdata["pm10 standard"],aqdata["pm25 standard"],aqdata["pm100 standard"],bme680.temperature, bme680.gas, bme680.relative_humidity,bme680.pressure,bme680.altitude]
        dwriter.writerow(data)
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
