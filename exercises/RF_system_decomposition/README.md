# RF System Analysis: nRF52840
**Student:** Niklas Etling (s2312830)  
**Device Page:** [Nordic nRF52840 Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf52840/page/keyfeatures_html5.html)

---

## 1. Overview
This project focuses on analyzing the internal RF architecture of the Nordic nRF52840 Bluetooth Low Energy (BLE) System-on-Chip (SoC). The goal is to understand the complete signal flow, tracing data from its digital state in memory to its transmission as electromagnetic radiation.

## 2. Hardware: nRF52840
* **Manufacturer:** Nordic Semiconductor
* **Protocol Support:** BLE, Thread, Zigbee, and 2.4GHz proprietary
* **Core Feature:** A highly integrated 2.4 GHz radio featuring a built-in Power Amplifier (PA) and Low Noise Amplifier (LNA).

## 3. Original RF Block Analysis

| RF Block | System Role | Impact if Missing |
| :--- | :--- | :--- |
| **RAM** | Information source and destination | No data to transmit therefore the system has no payload. |
| **EasyDMA** | Moves data between RAM and radio without CPU lag | CPU becomes a bottleneck and radio signal timing fails. |
| **CRC** | Error checking; ensures packets aren't corrupted | Undetected data corruption leads to junk data reaches the target. |
| **Whitening** | Signal scrambling for better synchronization | Receiver loses its lock on long strips of repeated bits. |
| **PA** | Boosts outgoing signals | Transmission range is significantly limited. |
| **LNA** | Catches faint incoming signals | Receiver sensitivity drops. |
| **ANT1 Pin** | Antenna Interface | No signals can be sent or received. |



## 4. Simplified Design Logic
My simplified model focuses on the **Information Journey**. I have abstracted the complex register-level control into a high-level signal flow to better visualize how data moves from a software variable to an antenna signal.

* **Data Pipeline Phase:** The EasyDMA, Packet Assembler, and Disassembler blocks are grouped together. This simplifies the high-speed movement and packetization logic into one stage.
* **Integrity and Security Phase:** The CRC and Whitening blocks are grouped here because their combined purpose is to ensure that accurate, synchronized data arrives at the destination.
* **Radio Front End Phase:** The antenna interface, RSSI, and the 2.4GHz Transmitter/Receiver are grouped into this phase. This abstracts the complex analog matching networks and transceiver circuitry into a single functional block that interacts with the physical world.

---

### Signal Flow Summary:
**RAM** $\rightarrow$ **Data Pipeline** $\rightarrow$ **Integrity/Security** $\rightarrow$ **Radio Front End** $\rightarrow$ **ANT1**
