#!/bin/bash
# This shell script will take a picture using the RPi camera and then it will
# save the image in the "camera" folder with specific DATE name to be then store in the server.
# Note: The camera is assumed to have its connection at the top so that the upside part of the picture corresponds
#       to the upside part of the camera that contains the connnection from camera to RPi


DATE=$(date  +%Y-%m-%d_%H%M)
echo "Picture name: $DATE"
raspistill -vf -o ~/Documents/access/camera/$DATE.jpg

# Call crop.py  to crop image that we just took
python crop.py $DATE

#$temp='_cropped'
#$name=$DATE$temp
#echo $name

DATE+=$'_cropped'

#.jpg added in add_ID.py
# Call add_ID.py  to upload image to the server
python add_ID.py $DATE
