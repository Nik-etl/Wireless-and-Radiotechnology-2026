import math
import os
import random
import time

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

# Ran on device acting as edge device.
# Load .env relative to this file so it works regardless of working directory.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# MQTT settings
broker = os.getenv("MQTT_BROKER", "")
topic = os.getenv("MQTT_TOPIC", "")
mqtt_port = int(os.getenv("MQTT_PORT", ""))

if not broker or not topic:
    raise RuntimeError(
        "Missing MQTT configuration. Check simulations/Grafana_Lab/.env for "
        "`MQTT_BROKER` and `MQTT_TOPIC`."
    )

# Temperature model parameters (simple smooth up/down wave).
temp_min = float(os.getenv("TEMP_MIN", "20"))
temp_max = float(os.getenv("TEMP_MAX", "35"))
center = (temp_min + temp_max) / 2.0
amplitude = (temp_max - temp_min) / 2.0

# One full cycle (up + down) duration.
period_seconds = float(os.getenv("WAVE_PERIOD_SECONDS", "60"))
# Random “weather/noise” around the wave.
noise_std = float(os.getenv("NOISE_STD", "0.2"))

update_interval_seconds = float(os.getenv("UPDATE_INTERVAL_SECONDS", "0.5"))
publish_qos = int(os.getenv("MQTT_QOS", "0"))

# MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect(broker, mqtt_port, 60)
mqtt_client.loop_start()

t0 = time.time()

while True:
    # Smooth sinusoidal temperature (gradually goes up and down).
    elapsed = time.time() - t0
    raw = center + amplitude * math.sin(2.0 * math.pi * elapsed / period_seconds)
    value = raw + random.gauss(0.0, noise_std)

    # Keep it in bounds so dashboards/threshold logic stay predictable.
    value = max(temp_min, min(temp_max, value))
    value_rounded = round(value, 2)

    # Publish to MQTT (send as string payload).
    mqtt_client.publish(topic, str(value_rounded), qos=publish_qos)
    print("Published to MQTT:", value_rounded)

    time.sleep(update_interval_seconds)