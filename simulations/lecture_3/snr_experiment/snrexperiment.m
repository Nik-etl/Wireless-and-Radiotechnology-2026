% Parameters

fs = 1000; % Sampling frequency in Hz

t = 0:1/fs:1-1/fs; % This creates exactly 1000 samples % Time vector

f_c = 50; % Carrier frequency in Hz

snr_vals = [10, 5, 0, -5];

%% 2. Generate Binary Message
num_bits = 10;

% Create 10 bits and stretch them to match the length of t
bits = randi([0 1], 1, num_bits);
bit_samples = floor(length(t)/num_bits);
message_signal = repelem(bits, bit_samples);
message_signal = message_signal(1:length(t)); % Ensure lengths match

%% 3. ASK Modulation
carrier = sin(2 * pi * f_c * t);
modulated_signal = message_signal .* carrier;

%% 4. Loop through SNR values & Plot
figure('Name', 'SNR Impact Analysis', 'Color', 'w');
for i = 1:4
    % Add AWGN Noise
    received = awgn(modulated_signal, snr_vals(i), 'measured');
    
    % Simple Demodulation (Rectify + Smooth/Threshold)
    envelope = movmean(abs(received), 20);
    demodulated = envelope > 0.3; % Thresholding
    
    % Plotting Received Signal
    subplot(4, 2, 2*i-1);
    plot(t, received);
    title(['Received (SNR = ', num2str(snr_vals(i)), ' dB)']);
    grid on; axis([0 1 -2 2]);
    
    % Plotting Demodulated Result
    subplot(4, 2, 2*i);
    plot(t, demodulated, 'LineWidth', 1.5, 'Color', 'r');
    hold on;
    plot(t, message_signal, 'k--', 'LineWidth', 1);
    title(['Demodulated vs Original']);
    grid on; axis([0 1 -0.2 1.2]);
    legend('Demodulated', 'Original');
end
drawnow; % Force MATLAB to render the figure
%%
ver
