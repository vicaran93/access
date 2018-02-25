#!/bin/bash

# This shell script will test if the camera is taking a picture and saving it in the correct place
# Steps:
# 1. Take a picture using the RPi camera
# 2. Save the image in the "camera" folder.
# 3. Check that the image was actually saved


DATE=$(date  +%Y-%m-%d_%H%M)
#raspistill -vf -o ~/Documents/access/camera/$DATE.jpg
raspistill -ISO 800 -ss 80000 -br 80 -co 100 -vf -o ~/Documents/access/camera/$DATE.jpg
python check_img.py $DATE
