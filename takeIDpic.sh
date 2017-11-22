#!/bin/bash

# This shell script will take a picture using the RPi camera and then it will
# save the image in the "camera" folder with specific DATE name to be then store in the server.
# Note: The camera is assumed to have its connection at the top so that the upside part of the picture corresponds
#       to the upside part of the camera that contains the connnection from camera to RPi


DATE=$(date  +%Y-%m-%d_%H%M)
#echo "$DATE"
raspistill -vf -o ~/Documents/access/camera/$DATE.jpg

# Call add_ID.py  to upload image to the server
python add_ID.py $DATE
