import adafruit_bme680
import time
import board

# Create sensor object
i2c = board.I2C() # Uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25
start = time.time()
print(start)
print("")

while time.time() <= (start + 10):
	now = time.time() - start
	print(now, " seconds have passed","Temperature: %0.1f C" % bme680.temperature,"Gas: %d ohm" % bme680.gas,"Humidity: %0.1f %%" % bme680.relative_humidity,"Pressure: %0.3f hPa" % bme680.pressure,"Altitude = %0.2f meters" % bme680.altitude)

	
	
	
	
	time.sleep(2)
	
