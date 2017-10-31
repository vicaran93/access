import RPi.GPIO as GPIO
import time

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)
	return

for i in range(0,10):
	blinkOnce(26)

GPIO.cleanup()
