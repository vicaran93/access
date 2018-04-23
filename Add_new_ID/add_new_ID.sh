#!/usr/bin/env bash

IMAGE_NAME=$1
# upload image to the server
python ./Add_new_ID/upload_RPi.py $IMAGE_NAME

# Delete all files
#rm $DATE #remove black and white image
#DATE=${DATE%???}; # remove last three characters (_bw)
#rm $DATE #remove cropped image
#DATE=${DATE%????????}; # remove last 8  characters (_cropped)
#rm $DATE #remove original image


