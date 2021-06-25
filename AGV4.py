import RPi.GPIO as GPIO
import time
print ("Servo Motor Example")
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
p=GPIO.PWM(17,50)
p.start(1)

for x in range(0,3):
	print("count = " +str(x))
	print("12.5");
	p.ChangeDutyCycle(12.5)
	time.sleep(2)

	print("10.0")
	p.ChangeDutyCycle(10.0)
	time.sleep(2)

	print("7.5")
	p.ChangeDutyCycle(7.5)
	time.sleep(2)

	print("5.0")
	p.ChangeDutyCycle(5.0)
	time.sleep(2)

	print("2.5")
	p.ChangeDutyCycle(2.5)
	time.sleep(2)

print("GPIO.cleanup()")
GPIO.cleanup()
