import RPi.GPIO as GPIO
import time

print ("Servo Motor")
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setwarnings(False)

p=GPIO.PWM(17,100)
p.start(5)
try:
	while True:
		angle=int(input("Enter Angle(0 to 180): "))
		duty= float(angle)/10.0+2.5
		p.ChangeDutyCycle(duty)
		time.sleep(0.5)
except KeyboardInterrupt:
	print("GPIO.cleanup()")
	GPIO.cleanup()
