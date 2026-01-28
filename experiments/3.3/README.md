# BLE Device Analysis & Site Survey

## 1. Introduction
This project investigates the signal propagation characteristics of Bluetooth Low Energy (BLE) devices in indoor and outdoor environments.
**Tools Used:** nRF Connect / BLE Scanner (iOS)
**Device:** iPhone
**Target Devices:** AirPods Pro, JBL Tune 770

## 2. Analysis

### RSSI vs. Distance Relationship
* **Proximity Drop:** Moving from **2 cm** (-30 dBm) to **1 m** (-53 dBm) resulted in a massive ~23 dB drop. This shows that RSSI degrades most rapidly in the first meter of transmission.
* **The "Wall" Surprise:** Interestingly, the signal through an indoor wall at 5m (-60 dBm) was *stronger* than the signal outdoors at just 1m (-71 dBm).

### Environmental Impact (Multipath vs. Free Space)
* **Indoor Reflections:** The stronger indoor signal suggests **Multipath Propagation**. Inside a room, Bluetooth signals bounce off walls and furniture, effectively reaching the receiver from multiple angles, which can help maintain connection strength.
* **Outdoor Attenuation:** Outdoors, there are no walls to reflect the signal. Energy that doesn't hit the phone directly is lost to the environment. Additionally, at 2.4 GHz, the human body (which is mostly water) is a significant blocker. If the user's body was between the phone and the AirPods during the outdoor test, it would explain the sharp drop to -71 dBm.

## 3. Security & Privacy
### BLE Tracking Risks
Bluetooth Low Energy devices broadcast "Advertisement Packets" roughly 3 times per second to announce their presence.
* **Risk:** Retailers and malicious actors can use these packets to track a user's movement through a shopping mall or city.
* **Mitigation (MAC Randomization):** To prevent this, modern devices (like the iPhone and AirPods detected) use **Randomized MAC Addresses**. Instead of broadcasting a permanent hardware ID, they rotate their identifier (UUID) every 15-30 minutes, making long-term tracking difficult.

### Passive Scanning
As demonstrated in this experiment, it is possible to detect and identify specific hardware (e.g., "JBL Tune 770") without ever pairing with it. This information could be used for "Device Fingerprinting" to identify potential theft targets or profile a user's tech ecosystem.
