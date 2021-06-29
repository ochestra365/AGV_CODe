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
위쪽은 시간측정, 아래쪽은 소팅코드(의사코드에 가까움)->일요일까지 해내야 함.
~~~
import RPi.GPIO as GPIO
import time

Conveyor20=20
Motor16=16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Conveyor20,GPIO.OUT)
GPIO.setup(Motor16,16)
p=GPIO.PWM(Motor16,50)
p.start(0)

#컨베이어 벨트 굴러가게 함.
def Conveyor_GO():
    while True:
        GPIO.output(Conveyor20,True)
        print("컨베이어 가동중")
        time.sleep(1)
#3초간 컨베이어 벨트 멈추게 함. 이유는 DB에 데이터를 보내는 대기시간이 3초라서
def Conveyor_Stop():
    for i in range(0,3)
        GPIO.output(Conveyor20,False)
        print("%d"+str(i))
        time.sleep(1)
#적외선 센서로 동작 센싱 및 색상 분류
def Sensing():
    pass

#모터로 불량품을 쳐내기
def Sorting_Motor():
    while True:
        if(Sensing()!=True):
            Conveyor_Stop()
            #7.5가 90도라고 알고 있음.
            p.ChangeDutyCycle(7.5)
            time.sleep(3)
            p.ChangeDutyCycle(0)
            Conveyor_GO()
        else:
            Conveyor_GO()
if(__name__=='__main__'):
    try:
        Conveyor_GO()
        Sensing()
        Sorting_Motor()
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()

~~~
