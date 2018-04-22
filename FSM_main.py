#!/usr/bin/python
import RPi.GPIO as GPIO
import os
from datetime import datetime,timedelta
import display
import IR

# This method uses pin 18 to check its input; 10 times every second
# initialize input pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) # EXIT BUTTON
GPIO.setup(4, GPIO.IN)  # USER INPUT
#GPIO.setup(17, GPIO.IN) # NEW ID
GPIO.add_event_detect(17, GPIO.RISING)# USER INPUT
#GPIO.setup(27, GPIO.IN) # RESET
GPIO.add_event_detect(27, GPIO.RISING)# USER INPUT
GPIO_TRIGGER = 6
GPIO.setup(GPIO_TRIGGER, GPIO.IN,pull_up_down=GPIO.PUD_UP) # set GPIO direction (IN / OUT)
# x = GPIO.input(18)
# print(x)



def change_when_positive_edge(pin, variable):
    if GPIO.event_detected(pin):
        return not variable
    else:
        return variable

def main():

    once = True
    flag2 = True
    flag=1 # do not init to 1 or 0


    ''' Applying FSM using IR sensor. This system also implements a RESET functionality to avoid the case where the IR sensor stops working'''
    # INITIALIZATION
    print_general_info = True
    print_general_info_SM = True
    picture_taken = False
    picture_taken_SM = False
    new_ID_mode = 0
    RESET = True

    # run every clock cycle
    while GPIO.input(18) == 0: # Blue button to break while loop

        sensor_trigger = IR.IR_input() # 0: ID  inserted  1: Nothing inserted
        user_trigger   = GPIO.input(4) # 0: Not pressed   1: User trigger button pressed

        new_ID_mode = change_when_positive_edge(17,new_ID_mode)#check positive edge on pin 17
        RESET = change_when_positive_edge(27,RESET) # positive edge of GPIO.input(27)

        print("sensor_trigger: "+sensor_trigger+" user_trigger:"+user_trigger+" new_ID_mode:"+new_ID_mode+" RESET:"+RESET)
        continue
        if not RESET:
            # STATE 0:
            if sensor_trigger == 1 and user_trigger == 0 and not picture_taken:

                if print_general_info:
                    print_general_info = False
                    print("Waiting for buttons to be pressed:\n1. First button (PIN4) to take a picture in 'compare mode' <sensor>.\n2. Second button (PIN17) to go into 'add new ID mode'. \n3. Test camera \n4. Test server communication \n5. EXIT/blue button (PIN18) to exit.")
            # STATE 1:
            elif (sensor_trigger == 0 or user_trigger == 1 ) and not picture_taken :

                picture_taken = 1
            # STATE 2:
            elif picture_taken:

                picture_taken = 0
            else:
                print("UNEXPECTED CASE")
                exit(0)
        else: # IF RESET
            # STATE 3
            if user_trigger == 0 :
                if print_general_info_SM:
                    print_general_info_SM = False
                    print("<< SAFE MODE >>")
                    print("Waiting for buttons to be pressed:\n1. Check ID -> 'compare mode'.\n2. Add ID --> 'new ID mode'. \n3. RESET \n5. EXIT (blue button)")

            # STATE 4
            elif user_trigger == 1 and not picture_taken_SM:
                # execute main program
                print("STATE 4: RUN PROGRAM")
                picture_taken_SM = True
                print_general_info_SM = True
    print("Blue button (PIN18) was pressed. Program finished.")
    GPIO.cleanup()


if __name__ == '__main__':
    main()
