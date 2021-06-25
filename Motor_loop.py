import time
import RPi.GPIO as GPIO

print("Servo Motor Test")

pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p= GPIO.PWM(pin, 50) #50Hz
p.start(2.5)

try:
  while True:
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
