from machine import *
from sht2x import *
import time
import machine
import wifiada
import sensor

i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)

relais = Pin('P21', mode=Pin.OUT)

while True:
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

	sensor.readuart()
	distance = sensor.readout()
	if distance != False:
        wifiada.sendDataWifi(distance)
