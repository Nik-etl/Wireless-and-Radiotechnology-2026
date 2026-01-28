# Local Wi-Fi Network Analysis

## 1. Introduction
This project analyzes the performance, coverage, and configuration of a local Residential Wi-Fi network.
**Tools Used:** Net Analyzer (iOS), AirPort Utility (Channel Scan)
**Device:** iPhone
**Router:** TP-Link


## 2. Analysis

### Band Steering and Coverage
The network utilizes dual-band technology.
* **Close Range:** At the "Desk" (-39 dBm), the device utilized the **5 GHz band (Ch 36)**. This band offers higher data rates but has lower wall penetration.
* **Long Range:** As I moved to the "Kitchen" and "Neighbor's room", the signal attenuated. The device automatically switched to the 2.4 GHz band (Ch 1)**. This confirms that 2.4 GHz has better propagation characteristics through obstacles, maintaining a usable connection (-65 dBm) where 5 GHz might have dropped.

### Bottleneck Identification (Speed vs. Signal)
The most important observation made is the **Speed Cap**.
* **Observation:** The Download Speed remained constant (~10-12 Mbps) regardless of whether the signal was atrong (-39 dBm) or weaker (-71 dBm).
* **Conclusion:** This indicates that the **Wi-Fi link is NOT the bottleneck**. The limitation is the Internet Service Provider (ISP) subscription bandwidth. The local network hardware is performing efficiently (low latency of 13ms), but it is throttled by the external WAN connection.

### Channel Allocation
* **2.4 GHz:** The network uses **Channel 1**. This is a standard non-overlapping channel (1, 6, 11).
* **Interference:** Channel 1 appears stable with consistent latency.

## 3. Recommendations
1.  **ISP Upgrade:** In order to access the full potential of the 5 GHz Wi-Fi hardware, I could upgrade the internet plan. The current router can handle much more than the current speed.
2.  **Router Placement:** The drop to -71 dBm at the neighbor's wall is acceptable, but indicates the edge of the coverage cell. If coverage is needed beyond this point, a Wi-Fi Extender or Mesh node should be placed near the Kitchen.
3.  **Security:** The network uses **WPA2** and could be upgraded to **WPA3** as it would would provide better protection against brute-force attacks.
