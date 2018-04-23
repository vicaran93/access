#!/bin/bash

IMAGE_NAME=$1

python ./Image_processing/crop_template.py $IMAGE_NAME # saves image as template.jpg


#python ./Add_new_ID/add_coordinates.py 'location.txt' #assumming Hassaan's code creates this file

NAME='template' # Hassaan's code saves template taken from $DATE as  template.png
python ./Image_processing/display.py $NAME # DISPLAY TEMPLATE
python ./Compare_ID/compare.py $IMAGE_NAME

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
