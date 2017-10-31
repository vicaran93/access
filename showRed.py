import RPi.GPIO as GPIO
import time

'''
This script blinks red light 10 times using pin 26
'''

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(0.5)
	GPIO.output(pin,False)
	time.sleep(0.5)
	return

for i in range(0,10):
	blinkOnce(26)

GPIO.cleanup()
