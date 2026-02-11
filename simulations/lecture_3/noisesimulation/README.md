# MATLAB Noise Removal Experiment

## Objective
To simulate the addition of Gaussian white noise to a 5Hz sinusoidal signal and recover the signal using a Low-pass Butterworth filter.

## Results
* **Original Signal**: A clean sine wave at 5Hz.
* **Noisy Signal**: The signal becomes distorted making the sine wave harder to distinguish.
* **Filtered Signal**: The Butterworth filter effectively removes frequencies above 10Hz, smoothing the wave back to its original shape with a slight phase shift.



## Evaluations & Observations
1. **Noise Impact**: The Gaussian noise adds random variations across the entire frequency spectrum. Since the signal is low-frequency: 5Hz, the noise significantly degrades the signal-to-noise ratio (SNR).
2. **Filter Performance**: The Low-pass filter (LPF) is ideal here because the noise is high frequency, while our signal is low frequency.
3. **Parameter Testing**: 
    * If the **Cutoff Frequency** is too low: 2Hz, the signal itself gets attenuated.
    * If the **Cutoff Frequency** is too high:100Hz, more noise is allowed to pass through.
