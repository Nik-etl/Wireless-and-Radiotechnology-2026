import paho.mqtt.client as mqtt
import requests
import os
from dotenv import load_dotenv

load_dotenv()

broker = os.getenv("MQTT_BROKER", "")
topic = os.getenv("MQTT_TOPIC", "")
mqtt_port = int(os.getenv("MQTT_PORT", ""))

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
threshold = float(os.getenv("TEMP_THRESHOLD", "28"))

def send_telegram(message):

    if not TOKEN or not CHAT_ID:
        print("Telegram not configured (missing TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID). Skipping alert.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)

def on_message(client, userdata, msg):

    temperature = float(msg.payload.decode())

    print("Temperature:", temperature)

    if temperature > threshold:

        alert = f"ALERT: High temperature {temperature} °C"

        print(alert)

        send_telegram(alert)

client = mqtt.Client()
client.connect(broker, mqtt_port)

client.subscribe(topic)

client.on_message = on_message

client.loop_forever()