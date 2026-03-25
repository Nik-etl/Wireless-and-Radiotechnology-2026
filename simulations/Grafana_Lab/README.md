## WirelessRadioTech - Grafana Lab (MQTT Temperature Monitoring)

In this lab I set up a very simple MQTT-based monitoring setup and then visualized the data in Grafana.

My chain is:

1. **Temperature publisher (simulated device)**: `simulations/Grafana_Lab/publisher.py` generates a smooth temperature signal (rise and fall) and publishes it to MQTT every ~0.5 seconds.
2. **MQTT broker**: `broker.emqx.io:1883` works as the message broker between the publisher and Grafana.
3. **Grafana dashboard**: Grafana receives the MQTT messages (from the configured data source) and plots the temperature over time.

## MQTT configuration

**MQTT topic used:** `niklas/iot/temperature`  
**Broker used:** `broker.emqx.io` (port `1883`)

## Grafana dashboard screenshot

Insert my Grafana screenshot here (for example: a time-series chart showing the temperature values).  
`(Add a screenshot in this section when submitting.)`

## What is shown in the panel

In the main panel I plot the **temperature value vs time** coming from the MQTT topic above. The temperature signal in the publisher is not just random numbers: it uses a smooth waveform and adds a bit of noise, so the chart looks more like a real sensor trend. If the panel includes a threshold/limit line, then it can also show when the temperature goes above `TEMP_THRESHOLD=28` from `.env`.

## Limitation: live-only MQTT visualization

With MQTT streaming, Grafana is great for **live monitoring**. However, if the pipeline is not storing the data in a time-series database (or similar), older measurements may not be available later. So the quality of graphs for longer history depends on whether data is kept beyond the current dashboard time window.

## Reflection Questions

### What is the role of Grafana in this system?

Grafana's role is to turn the incoming telemetry into something I can read easily. It plots the MQTT messages as a time series, so I can quickly see how the signal changes and whether it crosses thresholds.

### Why is MQTT useful for monitoring applications?

MQTT is useful because it is lightweight and follows publish/subscribe. The publisher does not need to know who is listening, and Grafana can subscribe only to the topic(s) I want to monitor.

### What is the difference between live monitoring and historical storage?

Live monitoring shows the newest data in near real time (usually limited to a time window). Historical storage keeps older data in a database, which makes it possible to query and analyze past behavior for longer periods.