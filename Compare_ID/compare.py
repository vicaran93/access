import requests,sys,os
#from PIL import Image

'''
 Input is the name without extension (i.e. test1 instead of test1.jpg)
'''

# Path variables
path="/home/pi/Documents/access/camera/"
print("------------------------ Entering Compare Mode ------------------------")
if len(sys.argv) == 2:
    image_name=sys.argv[1]+".jpg" #"test.jpg" in laptop or "test1_cropped.jpg" in RPi
    print("--> Comparing...")
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

print("\n--> SERVER RESPONSE:\n"+response.text) #TEXT/HTML
lines = response.text.split('\n')
info = lines[-4:-1]
info.append(lines[-1])

with open(path+'info.txt', 'a') as out_file:
    out_file.write(info)
    

if response.text[0] == "I": # Image received...
    pass
    #print("We got response back.Run test.py and show green LED!")
    #os.system('python test.py %s' % response.text);
    #os.system('%s %s' % ('ls', '-l'))
    #os.system('python showGreen.py')
elif response.text[0] == "E": # Eror detected...
    print("We got an error as a response. Show red LED!")
    os.system('python showRed.py')
print(response.status_code, response.reason) #HTTP
print("------------------------ Done ------------------------")