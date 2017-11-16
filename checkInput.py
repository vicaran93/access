import RPi.GPIO as GPIO

#This method uses pin 18 to check its input; 10 times every second
#initialize input pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.IN)

#x = GPIO.input(18)
#print(x)

while GPIO.input(18) == 0:
	if GPIO.input(4) == 1: #pressed
		print("PIN4 pressed")
	if GPIO.input(17) == 1: #pressed
		print("PIN17 pressed")
	if GPIO.input(27) == 1: #pressed
		print("PIN27 pressed")
print("PIN18 was pressed")
GPIO.cleanup()
