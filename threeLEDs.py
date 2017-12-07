import RPi.GPIO as GPIO
import time,os

'''
This script blinks three UV LEDs. Pin 23,24,25
'''

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

def blinkOnce(pin1,pin2,pin3):
        #GPIO.output(pin1,True)
	#GPIO.output(pin2,True)
	#GPIO.output(pin3,True)
	print("Turn on UV LEDs for 20s..")
	time.sleep(2)        
	os.system('./takepicTest.sh')
	time.sleep(2) 
	
        #GPIO.output(pin1,False)
	#GPIO.output(pin2,False)
	#GPIO.output(pin3,False)
	print("Turn off LEDs")
        return
		
blinkOnce(23,24,25)

GPIO.cleanup()
