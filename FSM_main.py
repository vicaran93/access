#!/usr/bin/python
import RPi.GPIO as GPIO
import os, sys, subprocess, time
from datetime import datetime,timedelta
#import display
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/IR_sensor') #, avg_white_filter
import IR
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/Image_processing') #, avg_white_filter
import average_white_test

# This method uses pin 18 to check its input; 10 times every second
# initialize input pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) # EXIT BUTTON
GPIO.setup(4, GPIO.IN)  # USER INPUT  compare
GPIO.setup(17, GPIO.IN) # NEW ID
GPIO.add_event_detect(17, GPIO.RISING, bouncetime=1000)# USER INPUT new ID
GPIO.setup(27, GPIO.IN) # RESET
GPIO.add_event_detect(27, GPIO.RISING,  bouncetime=1000)# USER INPUT Reset
GPIO_TRIGGER = 6
GPIO.setup(GPIO_TRIGGER, GPIO.IN,pull_up_down=GPIO.PUD_UP) # set GPIO direction (IN / OUT)
# x = GPIO.input(18)



def change_when_positive_edge(pin, variable):

    if GPIO.event_detected(pin):
        print(" POSITIVE EDGE DETECTED")
        if pin == 17:
            print("Changing new_ID_mode to:"+str(not variable))
            if not variable:
                print("-> SYSTEM ENTERING NEW ID MODE")
            else:
                print("-> SYSTEM EXITING NEW ID MODE")
        if pin == 27:
            print("Changing RESET to:"+str(not variable))
            if not variable:
                print("-> SYSTEM DISABLING IR SENSOR")
            else:
                print("-> SYSTEM ENABLING IR SENSOR")
        return not variable
    else:
        return variable
def main_function(min_threshold,max_threshold,new_ID_mode):

    ID = str(raw_input("Please enter ID number (4 digits):"))
    ID = str(ID).zfill(4)
    subprocess.call(['bash', 'take_pic_and_convert_to_BW.sh', ID])

    # Get name of black and white image of the ID
    ID_name = str(ID) + "_cropped_bw"
    # run filter
    filter_passed = average_white_test.filter(min_threshold, max_threshold, ID_name)
    print("filter_response: " + str(filter_passed))
    if filter_passed:
        if new_ID_mode:
            subprocess.call(['bash', './Add_new_ID/add_new_ID.sh', ID_name])
        else:
            subprocess.call(['bash', './Compare_ID/compare_ID.sh', ID_name])

    else:
        os.system('python ./LEDs/showRed.py')


def main():
    '''
        Applying FSM using IR sensor. This system also implements a RESET functionality to avoid the case where
        the IR sensor stops working
    '''
    # INITIALIZATION
    print_general_info = True
    print_general_info_SM = True
    picture_taken = False
    picture_taken_SM = False
    new_ID_mode = False
    RESET = False

    # GLOBAL VARIABLES
    min_threshold = 0.01
    max_threshold = 0.2
    first_time_in_S2 = True

    # run every clock cycle
    while GPIO.input(18) == 0: # Blue button to break while loop

        sensor_trigger = IR.IR_input() # 0: ID  inserted  1: Nothing inserted
        user_trigger   = GPIO.input(4) # 0: Not pressed   1: User trigger button pressed

        new_ID_mode = change_when_positive_edge(17,new_ID_mode)#check positive edge on pin 17
        RESET = change_when_positive_edge(27,RESET) # positive edge of GPIO.input(27)

        #print("sensor_trigger: "+str(sensor_trigger)+" user_trigger:"+str(user_trigger)+" new_ID_mode:"+str(new_ID_mode)+" RESET:"+str(RESET))
	    #time.sleep(1)  # pause
        #continue
        if not RESET:
            # STATE 0:
            if sensor_trigger == 1 and user_trigger == 0 and not picture_taken:
                if print_general_info:
                    print("STATE 0:")
                    print_general_info = False
                    print("System ON:\n1. Check ID -> 'compare mode'.\n2. Add ID --> 'new ID mode'. \n3. RESET \n5. EXIT (blue button)")
            # STATE 1:
            elif (sensor_trigger == 0 or user_trigger == 1 ) and not picture_taken :
                # Run program
                print("STATE 1:")
                print("ID inserted ->Running program")

                t1 = datetime.now()

                main_function(min_threshold, max_threshold, new_ID_mode)

                t2 = datetime.now()
                delta = t2 - t1 - timedelta(seconds=10)- timedelta(seconds=9)
                # - timedelta(seconds=10) # 10 seconds of showing Red or Green LEDs minus 3 displays
                if not new_ID_mode:
                    delta = delta - timedelta(seconds=3) # subtract displaying template time
                print("Total Runtime:" + str(delta.seconds) + " s")

                picture_taken = 1

            # STATE 2:
            elif picture_taken:

                if first_time_in_S2:
                    print("STATE 2!\nPlease take out the ID.")
                    first_time_in_S2 = False

                if sensor_trigger == 1 and user_trigger == 0: # ID out
                    picture_taken = 0 # transition to state 0
                    first_time_in_S2 = True
                    new_ID_mode = False
                    time.sleep(1)  # take a pause before transitioning to state 0 in case ID triggers sensor while removing it
		    print_general_info = True
            else:
                print("UNEXPECTED CASE")
                exit(0)
        else: # IF RESET
            # STATE 3
            if user_trigger == 0 :
                if print_general_info_SM:
                    print_general_info_SM = False
                    print("<< SAFE MODE >>\nSTATE 3:\n")
                    print("Waiting for buttons to be pressed:\n1. Check ID -> 'compare mode'.\n2. Add ID --> 'new ID mode'. \n3. RESET \n5. EXIT (blue button)")

            # STATE 4
            elif user_trigger == 1 and not picture_taken_SM:
                # execute main program
                print("STATE 4: ")

                t1 = datetime.now()

                main_function(min_threshold, max_threshold, new_ID_mode)

                t2 = datetime.now()
                delta = t2 - t1  # - timedelta(seconds=10) # 10 seconds of showing Red or Green LEDs
                print("Total Runtime:" + str(delta.seconds) + " s")

                picture_taken_SM = True
                print_general_info_SM = True
    print("Blue button (PIN18) was pressed. Program finished.")
    GPIO.cleanup()


if __name__ == '__main__':
    main()
