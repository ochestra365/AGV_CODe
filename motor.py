import RPi.GPIO as GPIO
from gpiozero import Servo
import time

motor=Servo(17)
GPIO.setwarnings(False)

while True:
	print('모터 회전방향 : Forward')
	motor.max()
	time.sleep(5)
