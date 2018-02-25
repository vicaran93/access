#!/usr/bin/python
import RPi.GPIO as GPIO
import os
from datetime import datetime,timedelta

# This method uses pin 18 to check its input; 10 times every second
# initialize input pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

# x = GPIO.input(18)
# print(x)

once = True
flag2 = True

flag=1 # do not init to 1 or 0

while GPIO.input(18) == 0: # Blue button to break while loop
    if flag2:
        flag2 = False
        print("Waiting for buttons to be pressed:\n1. First button (PIN4) to take a picture in 'compare mode' <sensor>.\n2. Second button (PIN17) to go into 'add new ID mode'. \n3. Test camera \n4. Test server communication \n5. EXIT/blue button (PIN18) to exit.")
    if GPIO.input(4) == 1: #first button
        if once:
            print("First button (PIN4) pressed. Entering 'compare mode' ")
	    t1 = datetime.now()
            os.system('./Compare_ID/compare_mode.sh')
	    t2 = datetime.now()
	    delta = t2 - t1 # - timedelta(seconds=10) # 10 seconds of showing Red or Green LEDs
	    print("Time taken:"+str(delta.seconds)+" s")

            once = False
            flag = 0
	    flag2 = True

    if GPIO.input(17) == 1:  # second button
        if once:
            print("Second button (PIN17) pressed. ")
            # Running showRed.py: os.system('python showRed.py')
            print("Entering new ID mode! Press: \n 1. First button (PIN4) to take a picture and upload it to server\n 2. RESET button to exit new ID mode")
            while GPIO.input(27) == 0:  # Third button to break while loop
                if GPIO.input(4) == 1:  # first button
                    if once:
                        print("First button (PIN4) pressed. Taking and adding  new ID  picture...")
			#SECONDS=0
			t1 = datetime.now()
                        os.system('../Add_new_ID/add_new_ID_mode.sh')
                        #print("Picture was taken") #assuming it was taken correctly (check ways to print a better status e.g. error variables)
			#duration=$SECONDS
			#echo "Time taken was: $(($duration / 60)) minutes and $(($duration % 60)) seconds."
			t2 = datetime.now()
			delta = t2 - t1 - timedelta(seconds=10) # 10 seconds of showing Red or Green LEDs
			print("Time taken:"+str(delta.seconds)+" s")
                        once = False
                        flag = 0
                        break #exit while loop
            # Setting up flags
            once = False
            flag = 0
	    flag2 = True #To show msg "Waiting to press.."

    #Third button is just for reset
    #if GPIO.input(27) == 1:  # third button
    #    if once:
    #        print("Third button (PIN27) pressed.")
            #print("Picture was taken")
    #        once = False
    if GPIO.input(23) == 1: # test camera
	if once:
            print("Test: Camera (PIN23)")
	    os.system('../Tests/test_camera.sh')

            once = False
            flag = 0
	    flag2 = True

    if GPIO.input(24) == 1: # test server
	if once:
            print("Test: Server Connection (PIN24)")
	    os.system('python ../Tests/test_server.py')

            once = False
            flag = 0
	    flag2 = True


    if flag == 0:
            once = True
            flag = 1
print("Blue button (PIN18) was pressed. Program finished.")
GPIO.cleanup()
