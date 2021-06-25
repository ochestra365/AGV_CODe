#-*- coding: utf-8*-
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json
import datetime as dt
import random
from typing import OrderedDict


Motor17=17
rnum=random.randint(0,100)

dev_id='MACHINE02'
broker_address='210.119.12.99'
pub_topic='factory1/machine2/data/'

def send_data(param,motor):
	pub_data=json.dumps(raw_data,ensure_ascii=False,indent='\t')
	pass

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor17,GPIO.OUT)

def loop():
	while True:
		for i rangin(0,3):
			print("count="+str(i))
			
			
			time.sleep(2)

if __name__=='__main__':
	setup()
	send_data('CONN',None,None,None)
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()
