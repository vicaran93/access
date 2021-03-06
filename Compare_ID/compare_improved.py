import requests, sys, os

# from PIL import Image

'''
 Input is the name without extension (i.e. test1 instead of test1.jpg) This method sends the file name in a POST request
 to /compare_improved.php in the heroku app
'''

# Path variables
path = "/home/pi/Documents/access/camera/"
print("------------------------ Entering Compare Mode ------------------------")
if len(sys.argv) == 2:
    image_name = sys.argv[1] + ".jpg"  # "test.jpg" in laptop or "test1_cropped.jpg" in RPi
    print("--> Comparing...")
else:
    print("No input detected in compare.py...using test1.jpg as image name")
    image_name = "test1_cropped.jpg"  # using test1.jpg does not work due to large image

print("-> Sending File Name: "+str(image_name))

final_path = path + image_name
# Load image:
# img = Image.open(final_path)
img = open(final_path, 'rb')

base_url = "https://sdp-lh18.herokuapp.com"
final_url = base_url + "/compare_improved.php"

response = requests.post(final_url, data = {'file_name':image_name})

print("\n--> SERVER RESPONSE:\n" + response.text)  # TEXT/HTML

''' WRITE DATA TO info.txt '''
lines = response.text.split('\n')
info = lines[-16:-4]
#info.append(lines[-1])
with open(path + 'info.txt', 'a') as out_file:
    for line in info:
        out_file.write(line + '\n')

check = lines[-3]
print("check is: "+str(check))
if response.text[0] == "I" and check[0] == "Y":  # Image received...
    print("We got match. Show green LED!")
    # os.system('python test.py %s' % response.text);
    # os.system('%s %s' % ('ls', '-l'))
    os.system('python ./LEDs/showGreen.py') # from Main or FSM_main - from this file :../LEDs/showGreen.py
elif response.text[0] == "E":  # Eror detected...
    print("We got an error as a response. Show red LED!")
    os.system('python ./LEDs/showRed.py')  # from Main or FSM_main - from this file :../LEDs/showGreen.py
elif check[0] == "N":
	print("NO MATCH!")
	os.system('python ./LEDs/showRed.py')  # from Main or FSM_main - from this file :../LEDs/showGreen.py
print(response.status_code, response.reason)  # HTTP
print("------------------------ Done ------------------------")
