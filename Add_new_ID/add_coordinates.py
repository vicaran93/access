import requests
import sys,os
from PIL import Image
from datetime import datetime

'''
 Image name should be pass through console i.e sys.argv[1]. It then opens file in "/home/pi/Documents/access/camera/"
 with the name provided as an input. This image is uploaded to serer using upload.php code in our Heroku app
'''

t1 = datetime.now()

# Path variables
path="/home/pi/Documents/access/camera/"
file_name="location.txt" 
final_path=path+file_name


base_url="https://sdp-lh18.herokuapp.com"
final_url=base_url+"/upload.php" #php code created to upload image in POST request

with open(final_path, 'rb') as f: response = requests.post(final_url, files={'userfile': f})

print("------------------------ Send Coordinates: ------------------------")
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

t2 = datetime.now()
delta = t2 - t1  # - timedelta(seconds=10) # 10 seconds of showing Red or Green LEDs
print("Total Runtime (Selecting better template):" + str(delta.seconds) + " s")
print("------------------------ Done uploading coordinates ------------------------")


