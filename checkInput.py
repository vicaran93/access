import RPi.GPIO as GPIO

#This method uses pin 18 to check its input; 10 times every second

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

GPIO.input(18)

#for i in range(4):

#	val = GPIO.input(18)
#	print(val)

GPIO.cleanup()
