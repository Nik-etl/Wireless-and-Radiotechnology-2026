import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
# Ran on device one acting as 
load_dotenv()

broker = os.getenv("MQTT_BROKER", "")
topic = os.getenv("MQTT_TOPIC", "")
mqtt_port = int(os.getenv("MQTT_PORT", ""))

def on_message(client,userdata,msg):

    value = msg.payload.decode()

    print("Cloud received:",value)

client = mqtt.Client()

client.connect(broker, mqtt_port)

client.subscribe(topic)

client.on_message = on_message

client.loop_forever()