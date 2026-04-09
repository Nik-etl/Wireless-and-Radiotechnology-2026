import paho.mqtt.client as mqtt
import random
import time

broker = "broker.emqx.io"
topic = "savonia/iot/temperature"

client = mqtt.Client()
client.connect(broker, 1883)

while True:
    temperature = round(random.uniform(20,30),2)
    message = f"{temperature}"

    client.publish(topic, message)

    print("Published:", message)

    time.sleep(5)