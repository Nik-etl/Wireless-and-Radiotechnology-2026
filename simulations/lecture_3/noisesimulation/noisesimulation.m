% Parameters

fs = 1000; % Sampling frequency in Hz

t = 0:1/fs:1; % Time vector

f_signal = 5; % Frequency of the sinusoidal signal in Hz

amplitude = 1; % Amplitude of the sinusoidal signal

% Generate the sinusoidal signal
signal = amplitude * sin(2 * pi * f_signal * t);

% Generate the noisy signal
noise = 0.5 * randn(size(signal)); % Generate random noise
noisy_signal = signal + noise; % Add noise to the original signal
  
% Designing a Butterworth filter
cutoff_frequency = 10;  % Hz
order = 4;              % Filter order

% Normalize the cutoff frequency by the Nyquist frequency (fs/2)
Wn = cutoff_frequency / (fs/2); 
[b, a] = butter(order, Wn, 'low');

% Apply the filter
filtered_signal = filter(b, a, noisy_signal);

%% 3 & 5. Plotting the Results
figure('Name', 'Signal Processing Results', 'NumberTitle', 'off');

% Original Signal
subplot(3, 1, 1);
plot(t, signal, 'LineWidth', 1.5);
title('Original 5Hz Sinusoidal Signal');
xlabel('Time (s)'); ylabel('Amplitude');
grid on;

% Noisy Signal
subplot(3, 1, 2);
plot(t, noisy_signal, 'Color', [0.8 0.3 0.3]);
title('Signal with Gaussian White Noise');
xlabel('Time (s)'); ylabel('Amplitude');
grid on;

% Filtered Signal
subplot(3, 1, 3);
plot(t, filtered_signal, 'k', 'LineWidth', 1.5);
title(['Filtered Signal (Low-pass Cutoff: ', num2str(cutoff_frequency), ' Hz)']);
xlabel('Time (s)'); ylabel('Amplitude');
grid on;
