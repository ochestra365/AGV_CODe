import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

LED2=2
LED3=3
LED4=4
LED7=7
BUTTON16=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED7,GPIO.OUT)
GPIO.setup(BUTTON16,GPIO.IN)

try:
	while True:
		if(GPIO.input(BUTTON16)==True):
			GPIO.output(LED2,True)
			GPIO.output(LED3,True)
			GPIO.output(LED4,True)
			GPIO.output(LED7,True)
		else:
			GPIO.output(LED2,False)
			GPIO.output(LED3,False)
			GPIO.output(LED4,False)
			GPIO.output(LED7,False)
except KeyboardInterrupt:
	GPIO.cleanup()
