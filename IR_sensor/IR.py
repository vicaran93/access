# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 6

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.IN)


def IR_input():

    if GPIO.input(GPIO_TRIGGER) == 0:
        print("Trigger is 0!")
    else:
        print("Trigger is 1!")

if __name__ == '__main__':
    try:
        while True:
            IR_input()
            time.sleep(1)

            # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("IR sensor input stopped by User")
        GPIO.cleanup()
