import os.path
import sys


if (len(sys.argv) == 2): #one input: the name of file to be checked
    file_name= sys.argv[1]
    # Path variables
    path = "C:/Users/Victor/Documents/UMass Amherst/Fall 2017/SDP/images/" # path without image name "/home/pi/Documents/access/camera/"
    image_name = file_name + ".jpg"  # "test.jpg" in laptop or "test1_cropped.jpg" in RPi
    print("Checking if: "+image_name+" exists")
    final_path = path + image_name

    exists = os.path.isfile(final_path)

    if exists == True:
        #show green LED
        print("Image file exists!")
        #os.system('python showGreen.py')
    else:
        print("Image file was not detected! Error")
        #os.system('python showRed.py')

else:
    print("Wrong input parameters! Cannot check if image file exists.")