from machine import *
from sht2x import *
import time
import machine
import wifiada
import sensor

i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)

relais = Pin('P8', mode=Pin.OUT)

while True:
	global humidity
	global temperature
	try:
		humidity = si7021.humidity()
		temperature = si7021.temperature()
		print(str(temperature) + " celcius")
		print(str(humidity) + " %")
		print("")
		if humidity <= 70:
			relais.value(1)
		else:
			relais.value(0)
		time.sleep(1)
	except OSError as e:
		print(e)
		time.sleep(2)

	sensor.readuart()
	distance = sensor.readout()
	if distance != False:
		print("inside me!")
        wifiada.sendDataWifi(distance)
