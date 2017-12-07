#!/bin/bash


DATE=$(date  +%Y-%m-%d_%H%M)
#echo "$DATE"
raspistill -w 2592 -h 1944 -ISO 800 -ss 80000 -br 80 -co 100 -vf -o ~/Documents/access/camera/$DATE.jpg
# -w 2592 -h 1944 -ISO 800 -ss 6000000 -br 80 -co 100
#raspiyuv  raspistil


