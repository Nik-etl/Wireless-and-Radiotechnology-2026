1. **Overview**
This project simulates and compares three distinct wireless technologies: WiFi (802.11b), Bluetooth, and Cellular (GSM). We analyze how signal strength, quality (SINR), and data capacity change as a function of distance

Technology,Frequency,Bandwidth,Tx Power,Range Simulated
WiFi,2.4 GHz,22 MHz,100 mW (20 dBm),1–100 m
Bluetooth,2.45 GHz,2 MHz,10 mW (10 dBm),0.5–10 m
Cellular,850 MHz,200 kHz,40 W (46 dBm),100–5000 m

2. **Observations**
- All technologies show a consistent downward slope on the logarithmic plot. This follows the 6dB rule, where as distance doubles the received power drops 6dB.

- Cellular signal is able to maintain higher power over much higher distances due to operating at a lower frequency.This is because Higher frequency systems experience greater path loss compared to lower frequencies.

- WiFi starts exactly 10dB higher than bluetooth, due to WiFi(100mW) consuming more power than bluetooth(10mW). 10x increase in watts = +10dB shift in the link budget.

- Wifi provides the highest peak data rate, but only at short distances.

- Cellular provides lowest peak speed but stays functional over 5km

3. **Conclusion**
Wireless engineering follows a fine balance of frequency, distance, and power among other variables. There is no one size fits all approach and every system has a trade-off. 
