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
flag2 = True

flag=1 # do not init to 1 or 0

while GPIO.input(18) == 0:
    if flag2:
	flag2 = False
	print("Waiting for buttons to be pressed..(press blue button to exit)")
    if GPIO.input(4) == 1:
        if once:
            print("PIN4 pressed. Running showGreen.py")
	    os.system('python showGreen.py')
            once = False
            flag = 0

    if GPIO.input(17) == 1:  # pressed
        if once:
            print("PIN17 pressed. Running showRed.py")
	    os.system('python showRed.py')
            once = False
            flag = 0

    if GPIO.input(27) == 1:  # pressed
        if once:
            print("PIN27 pressed.")
	    os.system('./takepic.sh')
	    print("Picture was taken")
            once = False

    if flag == 0:
            once = True
            flag = 1
print("PIN18 was pressed. Program finished.")
GPIO.cleanup()
