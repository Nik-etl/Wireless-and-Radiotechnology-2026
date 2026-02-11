n_samples = 10000;
B = 1e6;
R = 100;
T = 300; % Temperature in Kelvin

time = 0:1/B:(n_samples-1)/B;

thermal_noise = sqrt(4 * 1.28e-23 * T * R * B) * randn(1, n_samples);


plot(time, thermal_noise)

xlabel('Time (s)');
ylabel('Thermal Noise (V)');
title('Thermal Noise Signal');
grid on;

[psd, freq] = pwelch(thermal_noise, [], [], [], B)
semilogx(freq, 10*log10(psd))

xlabel('Frequency (Hz)');
ylabel('Power/Frequency (dB/Hz)');
title('Power Spectral Density of Thermal Noise');
grid on;
