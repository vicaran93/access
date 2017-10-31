#!/bin/bash

# This shell script will take a picture using the RPi camera and then it will 
# save the image in the "camera" folder.
# Note: the camera is assumed to have its connection at the top


DATE=$(date  +%Y-%m-%d_%H%M)
#echo "$DATE"
raspistill -vf -o ~/Documents/camera/$DATE.jpg

