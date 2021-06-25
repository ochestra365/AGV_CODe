import RPi.GPIO as GPIO
import time

pin17=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin17,GPIO.OUT)
p=GPIO.PWM(pin17,50)
p.start(0)
cnt=0
try:
	while True:
		p.ChangeDutyCycle(12.5) #최댓값
		time.sleep(1)
		p.ChangeDutyCycle(10.0)
		time.sleep(1)
		p.ChangeDutyCycle(7.5) #0
		time.sleep(1)
		p.ChangeDutyCycle(5.0)
		time.sleep(1)
		p.ChangeDutyCycle(2.5) #최솟값
		time.sleep(1)
		
except KeyboardInterrupt:
	p.stop()

GPIO.cleanup()
