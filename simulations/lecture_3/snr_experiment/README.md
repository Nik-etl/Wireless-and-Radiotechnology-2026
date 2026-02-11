# Lab: SNR Impact on Digital Demodulation

## Objective
To analyze how the Signal-to-Noise Ratio (SNR) influences the accuracy of recovery in an Amplitude Shift Keying (ASK) communication system.

## Methodology
1. **Message Generation:** A 10-bit binary sequence was generated and upsampled to match the 1000Hz sampling rate.
2. **Modulation:** Amplitude Shift Keying (ASK) was applied using a 50Hz carrier wave.
3. **Channel Noise:** Gaussian white noise was added at decreasing levels: 10dB, 5dB, 0dB, and -5dB.
4. **Demodulation:** Used envelope detection (moving average of rectified signal) followed by a threshold comparison to recover bits.

## Observations
* **SNR 10dB / 5dB:** The recovered signal is highly accurate. The nature of the carrier is clearly distinguishable from the noise floor.
* **SNR 0dB:** The noise power equals the signal power. Bit transitions become jittery, and small errors start to appear at bit edges.
* **SNR -5dB:** The noise power exceeds the signal power. The demodulator triggers false positives due to noise spikes, resulting in a high Bit Error Rate (BER).

## Conclusions
Effective communication requires the signal power to be significantly higher than the noise floor. As SNR decreases, simple thresholding fails.
