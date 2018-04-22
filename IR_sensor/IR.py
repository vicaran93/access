# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 6

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.IN,pull_up_down=GPIO.PUD_UP)


def IR_input():
    ''' Checks IR Sensor connected at GPIO 6. If response is 0, an ID has been detected, 1 otherwise. '''

    if GPIO.input(GPIO_TRIGGER) == 0:
        print("Trigger is 0!")
        return 0
    else:
        print("Trigger is 1!")
        return 1

if __name__ == '__main__':
    try:
        while True:
            return_result = IR_input()
            print("return_result: "+return_result)
            time.sleep(1)

            # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("IR sensor input stopped by User")
        GPIO.cleanup()
