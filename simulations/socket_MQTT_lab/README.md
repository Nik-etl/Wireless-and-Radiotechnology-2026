# Lab: Socket-to-MQTT Edge Gateway

**Student:** Niklas Etling  
**Course:** Wireless and Radio Tech. (IT–IoT BSc)  

### Scenario and Theoretical Devices
This lab models a **three-tier IoT architecture** using theoretical devices:
- **Device 1 – Sensor Node:** A temperature sensor device that connects over TCP to an edge gateway and periodically sends measurements.
- **Device 2 – Edge Gateway:** An intermediate node that receives raw sensor data over a socket, then republishes it to an MQTT broker.
- **Cloud/Backend Device:** A cloud-side MQTT subscriber that receives the published values and represents backend processing or monitoring.

In practice, each of these roles is implemented as a separate Python script that can be run on different physical machines or on the same machine with different terminal windows.

### Role of Each Script
- **`socket_sensor.py` (Device 1 – Sensor Node):**
  - Simulates a physical temperature sensor.
  - Opens a TCP client connection to the edge gateway (`SENSOR_SERVER_IP`, `SENSOR_SERVER_PORT`).
  - Periodically generates random temperature values and sends them as plain text.

- **`edge_server.py` (Device 2 – Edge Gateway):**
  - Acts as a TCP **server** for incoming sensor connections (`TCP_HOST`, `TCP_PORT`).
  - Forwards each received sensor value to the MQTT broker as an MQTT **publisher** on `MQTT_TOPIC`.
  - Conceptually represents an **edge computing device** that bridges local sensor networks to a cloud messaging system.

- **`MQTT_subscriber.py` (Cloud/Backend Device):**
  - Connects to the same MQTT broker as a **subscriber**.
  - Listens on `MQTT_TOPIC` and prints the received values to the console.
  - Represents a simple cloud-side monitoring or backend service.

### Configuration via `.env`
The `.env` file in this folder defines all network and broker parameters:
- **`TCP_HOST` / `TCP_PORT`**: Address on which the edge gateway listens for incoming sensor TCP connections.
- **`SENSOR_SERVER_IP` / `SENSOR_SERVER_PORT` / `SENSOR_SEND_INTERVAL_SECONDS`**: Where the sensor node connects and how often it sends data.
- **`MQTT_BROKER` / `MQTT_PORT` / `MQTT_TOPIC`**: MQTT broker endpoint and topic used by both the edge gateway (publisher) and the cloud subscriber.

By changing only the `.env` file, the same code can be reused with different IPs, ports, brokers, and message rates, reflecting different IoT deployment scenarios.

### Learning Objectives
- Understand how a **TCP socket-based sensor link** can be bridged into an **MQTT-based IoT cloud**.
- Identify the logical roles of **sensor node**, **edge gateway**, and **cloud/backend** in an IoT system.
- Practice designing and reasoning about **multi-device architectures** and protocol translation at the edge.

