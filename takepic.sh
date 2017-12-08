#!/bin/bash

# This shell script will take a picture using the RPi camera and then it will 
# save the image in the "camera" folder.
# Image is cropped using crop.py script and sent to the server using compare.py
# script.
# Note: the camera is assumed to have its connection at the top


DATE=$(date  +%Y-%m-%d_%H%M)
#DATE="template" #Assumes that we store the template in database every time with name template_crop_bw.jpg
#echo "$DATE"
#raspistill -vf -o ~/Documents/access/camera/$DATE.jpg
raspistill -ISO 800 -ss 80000 -br 80 -co 100 -vf -o ~/Documents/access/camera/$DATE.jpg

# Call crop.py  to crop image that we just took
python crop.py $DATE

DATE+=$'_cropped'

python img2bw.py $DATE

DATE+=$'_bw'

# Call add_ID.py  to upload image to the server
python add_ID.py $DATE

python compare.py $DATE


