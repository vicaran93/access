
import RPi.GPIO as GPIO
import time,os,sys
sys.path.insert(0,"/home/pi/Documents/access/Image_processing")
from PIL import Image
import numpy as np
import crop_new as cn

'''
This script blinks green light 10 times using pin 12
'''

def LED_and_img():
    #initialize the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.OUT)

    if len(sys.argv) < 2:
        sys.exit("No input detected! Name of the file without extension must be provided as input through console")

    file_name = sys.argv[1]
    code = file_name
    file_name = file_name+".jpg"


    print("------------------------ Taking Image ------------------------")
    GPIO.output(21, True)
    print("UV LED on!")
    # time.sleep(30) #0.5
    temp = "raspistill -ISO 400 -ss 160000 -br 80 -co 100 -vf -o ~/Documents/access/camera/" + file_name
    os.system(temp)
    GPIO.output(21, False)
    print("UV LED off and Img taken")
    print("------------------------ Done ------------------------")

    GPIO.cleanup()

    # Open image and convert to numpy array
    path = "/home/pi/Documents/access/camera/"
    # Load image:
    path_new = path + file_name
    path_to_send = path + code
    img = Image.open(path_new)

    img = np.array(img, dtype=np.float64)
    sys.exit()
    cn.crop(img, path_to_send)


if __name__ == "__main__":
    LED_and_img()
