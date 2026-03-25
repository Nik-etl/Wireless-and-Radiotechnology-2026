## WirelessRadioTech - Grafana Lab 2 (PID control with MQTT)

In this lab I made a simple closed-loop control system and tried to visualize it in Grafana. I used MQTT to send the signals and Grafana to plot them.

### What I simulated

I made three parts:

1. **Reference signal `r(t)` (input)**  
   In `simulations/Grafana_Lab_2_multiple_sensor/publisher.py` I generate a repeating square wave:
   - HIGH for 20 seconds
   - LOW for 10 seconds  
   (repeats every 30 seconds)

2. **PID controller**  
   The controller tries to make the output `y(t)` follow `r(t)`. It uses the error:
   `e(t) = r(t) - y(t)`

   PID output:
   `u_control(t) = Kp*e(t) + Ki*integral(e) + Kd*d(e)/dt`

3. **Plant / output model (`y(t)`)**  
   The plant is a first-order system. In the code, `y` moves smoothly toward `u_control` with time constant `tau_seconds`. That is why the output is not an instant step.

### What gets published to MQTT

The publisher sends three numeric signals:
- `MQTT_TOPIC` -> reference `r`
- `MQTT_TOPIC/output` -> plant output `y` (default)
- `MQTT_TOPIC/control` -> controller effort `u_control` (default)

### MQTT configuration

From `.env` in this folder:
- Broker used: `broker.emqx.io` (port `1883`)
- MQTT topic (reference): `niklas/sensor/unit`

### Grafana dashboard screenshot

Insert my Grafana screenshot here (example: a time series chart showing `r`, `y`, and `u_control` together).  
`(Add a screenshot in this section when submitting.)`

### What I look at in the panel

I plot `r`, `y`, and `u_control` on the same time range:
- `r(t)` is the square reference (0/1)
- `y(t)` is the curved output that should track the reference
- `u_control(t)` shows what the controller is doing during the transitions

### Limitation: live-only MQTT visualization

If Grafana is consuming MQTT as a live stream without long-term storage, it may only show data inside the dashboard time window. Historical analysis depends on whether the messages are stored in a time-series database (or similar backend).

## Reflection Questions

1. What is the role of Grafana in this system?
Grafana visualizes the MQTT values as a time series so I can compare the reference `r(t)`, the output `y(t)`, and the controller effort `u_control(t)`.

2. Why is MQTT useful for monitoring applications?
MQTT is lightweight and supports publish/subscribe. The publisher can send the control signals without knowing who is reading them, and Grafana only subscribes to the topics I want.

3. What is the difference between live monitoring and historical storage?
Live monitoring shows what is happening now (usually limited to the dashboard time range). Historical storage keeps old data longer so I can check past behavior and trends later.