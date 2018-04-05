#!/bin/bash
# This shell script will take a picture using the RPi camera and then it will
# save the image in the "camera" folder with specific DATE name to be then store in the server.
# Note: The camera is assumed to have its connection at the top so that the upside part of the picture corresponds
#       to the upside part of the camera that contains the connnection from camera to RPi


#SECONDS=0
#DATE=$(date  +%Y-%m-%d_%H%M)

# Get user input
echo "Please enter ID number (4 digits):"
read DATE
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

python ./LEDs/LED_and_pic.py $DATE



# Call crop.py  to crop image that we just took
python ./Image_processing/crop.py $DATE

#$temp='_cropped'
#$name=$DATE$temp
#echo $name

DATE+=$'_cropped'

python img2bw.py $DATE
#python image_processing.py $DATE
#python ./Image_processing/ip_color_segmentation.py $DATE

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


