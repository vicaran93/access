#!/bin/bash

# This shell script will take a picture using the RPi camera and then it will 
# save the image in the "camera" folder.
# Image is cropped using crop.py script and sent to the server using compare.py
# script.
# Note: the camera is assumed to have its connection at the top


DATE=$(date  +%Y-%m-%d_%H%M)
#DATE="template" #Assumes that we store the template in database every time with name template_crop_bw.jpg

python ./LEDs/LED_and_pic.py $DATE # From location of main.py

# Call crop.py  to crop image that we just took
python ./Image_processing/crop.py $DATE

DATE+=$'_cropped'

#python img2bw.py $DATE # This does not deal with the artifacts encountered in the imgs
#python image_processing.py $DATE
python ./Image_processing/ip_color_segmentation.py $DATE

DATE+=$'_bw'

python ./Image_processing/better_template.py $DATE #Hassaan code

python ./Add_new_ID/add_coordinates.py 'location.txt' #assumming Hassaan's code creates this file

NAME='template' # Hassaan's code saves template taken from $DATE as  template.png

# Call add_ID.py  to upload TEMPLATE to the server and then to compare
python ./Add_new_ID/add_ID.py $NAME
python ./Compare_ID/compare.py $NAME

# DELETE IMAGES IN RPi

#DATE+=$'.jpg'
# Delete all files
#rm $DATE #remove black and white image
#DATE=${DATE%???}; # remove last three characters (_bw)
#DATE+=$'.jpg'
#rm $DATE #remove cropped image
#DATE=${DATE%????????????}; # remove last 8+4  characters (_cropped.jpg)
#DATE+=$'.jpg'
#rm $DATE #remove original image
