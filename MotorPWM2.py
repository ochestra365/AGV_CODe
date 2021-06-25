import RPi.GPIO as GPIO
import time

PIN17=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN17,GPIO.OUT)
p=GPIO.PWM(PIN17,50)

p.start(0)

p.ChangeDutyCycle(3)
time.sleep(1)

p.ChangeDutyCycle(12)
time.sleep(1)

p.ChangeDutyCycle(75)
time.sleep(1)

while True:
	val = float(input("input(3~7.5~12) = "))

	if val == -1: break

	p.ChangeDutyCycle(val)

p.stop()

GPIO.cleanup()
