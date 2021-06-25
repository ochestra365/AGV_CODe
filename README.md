# AGV_CODe

~~~
#Library
import time
import datetime as dt
from typing import OrderedDict
import RPi.GPIO as GPIO
import random
import paho.mqtt.client as mqtt
import json

mortor = 21 # Raspberry pi PIN 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(mortor, GPIO.OUT)
cycles = GPIO.PWM(mortor, 50)

dev_id = 'MACHINE01'
broker_address = '210.119.12.92'
pub_topic = 'factory1/machine1/data/'

def send_data(result):
    
    currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #json data gen
    raw_data = OrderedDict()
    raw_data['DEV_ID'] = dev_id
    raw_data['PRC_TIME'] = currtime
    raw_data['PRC_MSG'] = result
    
    pub_data = json.dumps(raw_data, ensure_ascii=False, indent='\t')
    print(pub_data)
    #mqtt_publish
    client2.publish(pub_topic, pub_data)

def loop():
    while True:
        start = time.time()
        num = random.randrange(2,5)
        for i in range(num):
            cycles.start(0)
            cycles.ChangeDutyCycle(3)
            time.sleep(2)
            cycles.stop()
        WorkTime = time.time() - start
        send_data(WorkTime)

#mqtt inti
print('MQTT Client')
client2 = mqtt.Client(dev_id)
client2.connect(broker_address)
print('MQTT Client connected')

if(__name__ == '__main__'):
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
~~~
