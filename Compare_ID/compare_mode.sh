#!/bin/bash

# This shell script will take a picture using the RPi camera and then it will 
# save the image in the "camera" folder.
# Image is cropped using crop.py script and sent to the server using compare.py
# script.
# Note: the camera is assumed to have its connection at the top


#DATE=$(date  +%Y-%m-%d_%H%M)
# Get user input
echo "Please enter ID number (4 digits):"
read DATE

# CHECK USER INPUT
echo "Picture name: $DATE"
if [[ -n ${DATE//[0-9]/} ]]
then
    echo "Contains letters! Wrong ID"
    exit
fi
STRLENGTH=$(echo -n $DATE | wc -m)
#echo $STRLENGTH
if (( $STRLENGTH != 4 ))
then
    echo "Wrong number of characters"
    exit
fi
# CHECK PASSED



python ./LEDs/LED_and_pic.py $DATE # From location of main.py
python ./Image_processing/display.py $DATE # DISPLAY ORIGINAL IMAGE

# Call crop.py  to crop image that we just took
python ./Image_processing/crop.py $DATE

DATE+=$'_cropped'
python ./Image_processing/display.py $DATE # DISPLAY

python ./Image_processing/img2bw.py $DATE # This does not deal with the artifacts encountered in the imgs
#python image_processing.py $DATE
#python ./Image_processing/ip_color_segmentation.py $DATE

DATE+=$'_bw'
python ./Image_processing/display.py $DATE # DISPLAY BLACK AND WHITE IMAGE

python ./Image_processing/average_white_test.py $DATE # Average white
#python ./Image_processing/better_template.py $DATE #Hassaan code
python ./Image_processing/crop_template.py $DATE # saves image as template.jpg


#python ./Add_new_ID/add_coordinates.py 'location.txt' #assumming Hassaan's code creates this file

NAME='template' # Hassaan's code saves template taken from $DATE as  template.png
python ./Image_processing/display.py $NAME # DISPLAY TEMPLATE

# Call add_ID.py  to upload TEMPLATE to the server and then to compare
#python ./Add_new_ID/add_ID.py $NAME  # uploading through Heroku
python ./Add_new_ID/upload_RPi.py $NAME   # uploading through RPi  $TEMP_NUM for testing
python ./Compare_ID/compare.py $DATE



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
