#!/bin/bash
# This shell script will take a picture using the RPi camera and then it will
# save the image in the "camera" folder with specific DATE name to be then store in the server.
# Note: The camera is assumed to have its connection at the top so that the upside part of the picture corresponds
#       to the upside part of the camera that contains the connnection from camera to RPi


#SECONDS=0
DATE=$(date  +%Y-%m-%d_%H%M)
echo "Picture name: $DATE"
#raspistill -vf -q 100 -o ~/Documents/access/camera/$DATE.jpg
#raspistill -ISO 400 -ss 160000 -br 80 -co 100 -vf -o ~/Documents/access/camera/$DATE.jpg
python ./LEDs/LED_and_pic.py $DATE



# Call crop.py  to crop image that we just took
python ./Image_processing/crop.py $DATE

#$temp='_cropped'
#$name=$DATE$temp
#echo $name

DATE+=$'_cropped'

#python img2bw.py $DATE
#python image_processing.py $DATE
python ./Image_processing/ip_color_segmentation.py $DATE

DATE+=$'_bw'

# Call add_ID.py  to upload image to the server
#python ./Add_new_ID/add_ID.py $DATE
python ./Add_new_ID/upload_RPi.py $DATE

# Delete all files 
#rm $DATE #remove black and white image
#DATE=${DATE%???}; # remove last three characters (_bw)
#rm $DATE #remove cropped image
#DATE=${DATE%????????}; # remove last 8  characters (_cropped)
#rm $DATE #remove original image


