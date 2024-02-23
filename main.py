import sys
from Adafruit_IO import MQTTClient
from simple_ai import *
from uart import *

import time
import random

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "BasintonDinh"
AIO_KEY = "aio_dMYr62asGZ81989WUnAcKLlt5ox7"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
counterAI = 5
sensor_type = 0
ai_result = "NULL"

while True:
    # counter = counter - 1

    # if counter <= 0:
    #     counter = 10

    #     #TODO
    #     print("Random data is publishing...")

    #     if sensor_type == 0:
    #         print("Temperature data...")
    #         temp = random.randint(25, 35)
    #         client.publish("cambien1", temp)
    #         sensor_type = 1

    #     elif sensor_type == 1:
    #         print("Humidity data...")
    #         humi = random.randint(50, 80)
    #         client.publish("cambien2", humi)
    #         sensor_type = 2

    #     elif sensor_type == 2:
    #         print("Light data...")
    #         light = random.randint(0, 100)
    #         client.publish("cambien3", light)
    #         sensor_type = 0

    counterAI = counterAI - 1

    if counterAI <= 0:
        counterAI = 5
        previous_result = ai_result
        ai_result = maskDetector()
        print("AI Output: ", ai_result)
        if ai_result != previous_result:
            client.publish("ai", ai_result)

        readSerial(client)

    time.sleep(1)

    pass

