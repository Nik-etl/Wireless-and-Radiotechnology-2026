Niklas Etling 
s2312830

*nRF52840*

https://docs.nordicsemi.com/bundle/ps_nrf52840/page/keyfeatures_html5.html

1. **OVERVIEW**
A brief statement on the project goal: analyzing the internal RF architecture of the Nordic nRF52840 Bluetooth Low Energy (BLE) System-on-Chip (SoC) to understand signal flow from digital data to electromagnetic radiation.

2. **HARDWARE: nRF52840** 
- manufacturer: Nordic Semiconductor.

- Protocol Support: BLE, Thread, Zigbee, and 2GHz proprietary

- Core Feature: A highly integrated 2.4 GHz radio with a built-in Power Amplifier (PA) and Low Noise Amplifier (LNA).

3. **Original RF Block Analysis**

| RF Block | System Role | Impact if Missing |
| :--- | :--- | :--- |
| RAM| Information source and destination | No data to transmit  |
| EasyDMA | Moves data between RAM and radio without CPU lag | CPU becomes a bottleneck and the radio signal timing fails  |
| CRC | Error checking and ensures packets aren't corrupted.  | Undetected data corruption, junk data reaches the target|
| Whitening | Signal Scrambling and ensures data isn't lost in noise | Receiver loses it's lock on long strips of repeated bits |
| PA | Boosts outgoing signals | Range is significantly limited. |
| LNA | Catches faint incoming signals | Sensitivity drops |

| ANT1 Pin | Antenna Interface | No signals will be sent or recieved |

4. **Simplified Design Logic**
My simplified model focuses on the Information Journey. I have abstracted the complex register-level control into a high-level signal flow to better visualize how data moves from a software variable to an antenna signal.

- The easyDMA, Packet Assembler and Disassembler blocks are grouped together into the *Data Pipeline* phase. This is to simplify all of the packetization logic.

- The CRC and Whitening blocks are then grouped into the  Integrity and Security phase because their main purpose is to ensure the correct data will arrive at the target destination.

- The antenna interface, RSSI, 2.4GHz Transmitter and Receiver blocks are all grouped to the Radio Front End phase. This is to simplify the complex antenna matching network into a single block. 
