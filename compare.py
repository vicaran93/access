import requests,sys,os
#from PIL import Image

'''
 Input is the name without extension (i.e. test1 instead of test1.jpg)
'''

# Path variables
path="/home/pi/Documents/access/camera/"

if len(sys.argv) == 2:
    image_name=sys.argv[1]+".jpg" #"test.jpg" in laptop or "test1_cropped.jpg" in RPi
    print("Seding: "+image_name)
else:
    print("No input detected in compare.py...using test1.jpg as image name")
    image_name="test1_cropped.jpg" #using test1.jpg does not work due to large image
final_path=path+image_name
# Load image:
#img = Image.open(final_path)
img = open(final_path,'rb')

base_url="https://sdp-lh18.herokuapp.com"
final_url=base_url+"/compare.php"

with open(final_path, 'rb') as f: response = requests.post(final_url, files={'userfile': f})

print(response.text) #TEXT/HTML
if response.text[0] == "I": # Image received...
    print("We got response back. Show green LED!")
    os.system('python showGreen.py')
elif response.text[0] == "E": # Eror detected...
    print("We got an error as a response. Show red LED!")
    os.system('python showRed.py')
print(response.status_code, response.reason) #HTTP