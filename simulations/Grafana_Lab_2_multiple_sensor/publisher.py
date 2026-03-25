import os
import time

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

# Load .env relative to this file so it works regardless of working directory.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# MQTT settings
broker = os.getenv("MQTT_BROKER", "")
input_topic = os.getenv("MQTT_TOPIC", "")
output_topic = os.getenv("MQTT_OUTPUT_TOPIC", f"{input_topic}/output")
control_topic = os.getenv("MQTT_CONTROL_TOPIC", f"{input_topic}/control")
mqtt_port_raw = os.getenv("MQTT_PORT", "")

if not broker or not input_topic or not mqtt_port_raw:
    raise RuntimeError(
        "Missing MQTT configuration. Check simulations/Grafana_Lab_2_multiple_sensor/.env for "
        "`MQTT_BROKER`, `MQTT_PORT`, and `MQTT_TOPIC`."
    )

mqtt_port = int(mqtt_port_raw)

# Pulse configuration (hardcoded)
# Publish a repeating pulse: output is HIGH for `pulse_width_seconds` within each `pulse_period_seconds`.
pulse_period_seconds = 30.0
pulse_width_seconds = 20.0  # HIGH duration: 20s high + 10s low
pulse_low = 0.0
pulse_high = 1.0

# Publish rate
update_interval_seconds = 0.5
publish_qos = int(os.getenv("MQTT_QOS", "0"))

# Plant time constant: how quickly output y moves toward input u.
# Larger tau => slower (more curved) response.
tau_seconds = 3.0

# PID controller gains
# e = r - y
# u_control = Kp*e + Ki*integral(e) + Kd*d(e)/dt
Kp = 1.0
Ki = 0.4
Kd = 0.1

# MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect(broker, mqtt_port, 60)
mqtt_client.loop_start()

print(
    "Pulse publisher started. "
    f"Input='{input_topic}', Output='{output_topic}', Control='{control_topic}', period={pulse_period_seconds}s, width={pulse_width_seconds}s, "
    f"values: {pulse_low} -> {pulse_high}"
)

t0 = time.time()
last_update_time = t0
y = pulse_low
integral_e = 0.0
prev_e = 0.0

while True:
    now = time.time()
    elapsed = now - t0
    # Time within the current period:
    phase = elapsed % pulse_period_seconds
    r = pulse_high if phase < pulse_width_seconds else pulse_low

    # PID controller:
    # error e = r - y
    # integral term accumulates error over time
    e = r - y
    dt = now - last_update_time if last_update_time else update_interval_seconds

    integral_e += e * dt

    derivative_e = (e - prev_e) / dt if dt > 0 else 0.0
    u_control_raw = (Kp * e) + (Ki * integral_e) + (Kd * derivative_e)

    # Clamp controller output to actuator limits (0..1 here).
    u_control = max(pulse_low, min(pulse_high, u_control_raw))

    # Simple anti-windup:
    # if we had to clamp, adjust integral so that unclamped output matches the clamp.
    if Ki != 0.0 and u_control_raw != u_control:
        integral_e = (u_control - (Kp * e + (Kd * derivative_e))) / Ki

    # First-order "plant": y curves toward u_control with time constant tau.
    # y(t+dt) = y(t) + dt/tau * (u_control - y(t))
    last_update_time = now
    y = y + (dt / tau_seconds) * (u_control - y)
    prev_e = e

    # Publish as numeric strings so Grafana can parse as numbers.
    mqtt_client.publish(input_topic, str(r), qos=publish_qos)
    mqtt_client.publish(output_topic, str(round(y, 4)), qos=publish_qos)
    mqtt_client.publish(control_topic, str(round(u_control, 4)), qos=publish_qos)
    print(
        f"Published MQTT: r={r} -> y={round(y,4)} "
        f"(u_control={round(u_control,4)}, Ki*I={round(Ki*integral_e,4)}, Kd*dE={round(Kd*derivative_e,4)}, t={elapsed:.1f}s, dt={dt:.2f}s)"
    )

    time.sleep(update_interval_seconds)