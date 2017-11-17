#!/usr/bin/python
import RPi.GPIO as GPIO
import os

# This method uses pin 18 to check its input; 10 times every second
# initialize input pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

# x = GPIO.input(18)
# print(x)

once = True
pin4_pressed = False
pin17_pressed = False
pin27_pressed = False

while GPIO.input(18) == 0:
    if GPIO.input(4) == 1:  # pressed
        if pin17_pressed or pin27_pressed:
            # need to reset once to True
            once = True
            pin17_pressed = False
            pin27_pressed = False
        if once:
            print("PIN4 pressed. Running showGreen.py")
	    os.system('python showGreen.py')
            once = False
            pin4_pressed = True

    if GPIO.input(17) == 1:  # pressed
        if pin4_pressed or pin27_pressed:
            # need to reset once to True
            once = True
            pin4_pressed = False
            pin27_pressed = False
        if once:
            print("PIN17 pressed. Running showRed.py")
	    os.system('python showRed.py')
            once = False
            pin17_pressed = True

    if GPIO.input(27) == 1:  # pressed
        if pin4_pressed or  pin17_pressed:
            # need to reset once to True
            once = True
            pin4_pressed = False
            pin17_pressed = False
        if once:
            print("PIN27 pressed. Taking picture...")
	    os.system('./takepic.sh')
            once = False
            pin27_pressed = True

print("PIN18 was pressed. Program finished.")
GPIO.cleanup()
