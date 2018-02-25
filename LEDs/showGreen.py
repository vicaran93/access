import RPi.GPIO as GPIO
import time

'''
This script blinks green light 10 times using pin 12
'''

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT) #12

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(10) #0.5
	GPIO.output(pin,False)
	#time.sleep(0.5)
	return
print("Green LED on! (10s)")
for i in range(0,1):
	blinkOnce(21) #12

GPIO.cleanup()
