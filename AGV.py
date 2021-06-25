import RPi.GPIO as GPIO
import time

PIN17=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN17,GPIO.OUT)
p=GPIO.PWM(PIN17,50)
p.start(0)
try:
	while True:
		p.ChangeDutyCycle(1)
		print ("angle : 1")
		time.sleep(1)
		p.ChangeDutyCycle(5)
		print ("angle : 5")
		time.sleep(1)
		p.ChangeDutyCycle(8)
		print ("angle : 8")
		time.sleep(1)
except KeyboardInterrupt:
	p.stop()
GPIO.cleanup()
