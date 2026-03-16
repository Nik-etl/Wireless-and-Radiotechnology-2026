# Lab: MQTT-Based Telegram Alert System

**Student:** Niklas Etling  
**Course:** Wireless and Radio Tech. (IT–IoT BSc)  

### Scenario and Theoretical Devices
This lab models a simple **IoT monitoring chain** using theoretical devices:
- **IoT Sensor Device (theoretical):** A temperature sensor node somewhere in the field publishing readings to an MQTT broker.
- **MQTT Broker (cloud service):** A public MQTT broker (e.g. `broker.emqx.io`) acting as the messaging backbone between devices.
- **Alert/Notification Device (Telegram client):** A cloud-side application that subscribes to the MQTT topic and sends Telegram messages to a human operator when an alarm condition is met.

In the actual implementation, the *alert/notification device* is represented by a Python script running on a PC (or cloud VM) which connects to the MQTT broker and to the Telegram Bot API.

### Role of the Script
- **`alert_system.py`**: 
  - Connects as an MQTT **subscriber** to the broker specified in `.env`.
  - Listens to the configured topic (e.g. `arsenii/iot/temperature`) for incoming temperature values.
  - Compares each received temperature to a configured **threshold**.
  - When the threshold is exceeded, sends a Telegram message using the bot token and chat ID from `.env`.

### Configuration via `.env`
The following parameters are stored in `.env` to separate configuration from code:
- **`MQTT_BROKER` / `MQTT_PORT` / `MQTT_TOPIC`**: Address of the MQTT broker and topic to subscribe to.
- **`TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID`**: Credentials and destination for Telegram alerts.
- **`TEMP_THRESHOLD`**: Temperature value (in °C) above which an alert is triggered.

This separation allows the same code to be reused in different environments (different broker, topic, or recipient) by only changing the `.env` file.

### Learning Objectives
- Understand how **MQTT publish/subscribe** can be used to transport sensor data.
- See how a cloud-side application can act as an **application-layer gateway** between MQTT and a human messaging service (Telegram).
- Practice using **environment variables** for secure and flexible configuration of network endpoints and API secrets.

