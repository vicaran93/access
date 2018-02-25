
import RPi.GPIO as GPIO
import time,os,sys

'''
This script blinks green light 10 times using pin 12
'''

#initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

if len(sys.argv) < 2:
    print("No input detected!")
    sys.exit("No input detected! Name of the file without extension must be provided as input through console")

file_name = sys.argv[1]
file_name = file_name+".jpg"

def blinkOnce(pin):
	GPIO.output(pin,True)
	print("UV LED on!")
	#time.sleep(10) #0.5
	temp ="raspistill -ISO 400 -ss 160000 -br 80 -co 100 -vf -o ~/Documents/access/camera/"+file_name 
        os.system(temp)
	GPIO.output(pin,False)
	#time.sleep(0.5)
	print("UV LED off and Img taken")
	return

print("------------------------ Taking Image ------------------------")
for i in range(0,1):
	blinkOnce(21)
print("------------------------ Done ------------------------")

GPIO.cleanup()


