#!/bin/bash
# This shell script will take a picture using the RPi camera and then it will
# save the image in the "camera" folder.
# Image is cropped using crop.py script and converted to black and white
# Note: the camera is assumed to have its connection at the top


#DATE=$(date  +%Y-%m-%d_%H%M)
# Get user input
#echo "Please enter ID number (4 digits):"
#read DATE

#echo "Passed Arg 1:$1"

DATE=$1
# CHECK USER INPUT
#echo "Picture name: $DATE"
#if [[ -n ${DATE//[0-9]/} ]]
#then
#    echo "Contains letters! Wrong ID"
#    exit
#fi
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
