import requests
import sys,os
from PIL import Image

'''
 Image name should be pass through console i.e sys.argv[1]. It then opens file in "/home/pi/Documents/access/camera/"
 with the name provided as an input. This image is uploaded to serer using upload.php code in our Heroku app
'''

# Path variables
path="/home/pi/Documents/access/camera/"
image_name=sys.argv[1]+".jpg" #"test.jpg" in laptop or "test1_cropped.jpg" in RPi
final_path=path+image_name

# Load image:
img = Image.open(final_path)
#img = open(final_path,'rb')


base_url="https://sdp-lh18.herokuapp.com"
final_url=base_url+"/upload.php" #php code created to upload image in POST request

with open(final_path, 'rb') as f: response = requests.post(final_url, files={'userfile': f})

width, height = img.size
#print("Size of image sent is (wxh): "+ str(width)+" by "+str(height))
print("------------------------ Send Image: " +image_name+" ------------------------")
print("--> Response:")
print(response.text) #TEXT/HTML
if response.text == "Upload successful":
    pass
    # print("We got response back. File is uploaded!")
    #show green LED
    #os.system('python ../LEDs/showGreen.py') # if commented out, decrease delta time in main.py by 10 sec (line 34)
elif  response.text == "Upload error":
    print("Upload error detected")
    #show red LED
    os.system('python ../LEDs/showRed.py')
else: print("No response detected")

print(response.status_code, response.reason) #HTTP
print("------------------------ Done uploading: " + image_name + " ------------------------")