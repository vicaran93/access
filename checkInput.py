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

while GPIO.input(18) == 0: # Blue button to break while loop
    if flag2:
        flag2 = False
        print("Waiting for buttons to be pressed..(press blue button to exit)")
    if GPIO.input(4) == 1: #first button
        if once:
            print("First (PIN4) pressed. Running showGreen.py")
            os.system('python showGreen.py')
            once = False
            flag = 0

    if GPIO.input(17) == 1:  # second button
        if once:
            print("Second button (PIN17) pressed. ")
            # Running showRed.py: os.system('python showRed.py')
            print("Entering new ID mode! Press: \n 1. Blue button (PIN18) to exit mode\n 2. First button (PIN4) to take a picture and upload it to server ")
            while GPIO.input(18) == 0:  # Blue button to break while loop
                if GPIO.input(4) == 1:  # first button
                    if once:
                        print("First button (PIN4) pressed. Taking new ID  picture")
                        os.system('./takeIDpic.sh')
                        print("Picture was taken") #assuming it was taken correctly (check ways to print a better status e.g. error variables)
                        #os.system('python showGreen.py')
                        once = False
                        flag = 0
                        break #exit while loop
            # Setting up flags
            once = False
            flag = 0

    if GPIO.input(27) == 1:  # third
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
