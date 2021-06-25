import RPi.GPIO as GPIO
import time

PIN17=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN17,GPIO.OUT)

p=GPIO.PWM(PIN17,50)
p.start(0)
left_angle=12.5
cneter_angle=7.5
right_angle=2.5

def doAngle(angle):
	p.ChangeDutyCycle(angle)
#	print ("Angle : %d % angle)
	time.sleep(0.5)

try:
	while True:
		var = int(input("Enter L/R/C : "))
		if var =='R' or var == 'r':
			print ("Right")
			doAngle(right_angle)
		elif var=='L' or var=='l':
			print("Left")
			doAngle(left_angle)
		elif var == 'C' or var=='c':
			print("Center")
			doAngle(center_angle)
except KeyboardInterrupt:
	p.stop()
GPIO.cleanup()

