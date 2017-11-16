import RPi.GPIO as GPIO

#This method uses pin 18 to check its input; 10 times every second

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

x = GPIO.input(18)

print(x)

while GPIO.input(18) == 0:
	print("not pressed yet")
	
print("button was pressed")
GPIO.cleanup()
