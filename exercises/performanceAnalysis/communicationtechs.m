clear all;
close all;
%%  constants
G_t = 1;
G_r = 1;
c = 3*1e8;
Pn = 500*1e-6; %noise power

%% WIFI SIMULATION
f_wifi = 2.4*1e9; %IEEE 802.11b
BW_wifi = 22*1e6;
d_wifi = 1:5:100;
P_t_wifi = 100*1e-3;
lamb_wifi = c/f_wifi;

Pr = P_t_wifi * G_r * G_t * (lamb_wifi ./ (4 * pi * d_wifi)).^2; %received power
Pr_wifi_dB = 10 * log10(Pr/0.001);
plot(d_wifi, Pr_wifi_dB);
xlabel('Distance (m)');
ylabel('Received Power (dBm)');
title('Received Power vs Distance for WiFi');

snr = Pr/Pn %signal noise ratio
snr_dB = 10 * log10(snr);
% Plot the SNR in dB against distance
figure;
plot(d_wifi, snr_dB);
xlabel('Distance (m)');
ylabel('SNR (dB)');
title('SNR vs Distance for WiFi');


% Calculate the capacity of the channel using the Shannon formula
capacity = BW_wifi * log2(1 + snr); 
capacity_dB = 10 * log10(capacity);
% Plot the channel capacity in dB against distance
figure;
plot(d_wifi, capacity_dB);
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('Channel Capacity vs Distance for WiFi');

%% BLUETOOTH SIMULATION
f_bluetooth = 2.45*1e9; %IEEE 802.11
BW_bluetooth = 2*1e6;
d_bluetooth = 0.5:0.5:10;
P_t_bluetooth = 10*1e-3;
lamb_bluetooth = c/f_bluetooth;

Pr_bluetooth = P_t_bluetooth * G_r * G_t * (lamb_bluetooth ./ (4 * pi * d_bluetooth)).^2; %received power
Pr_bluetooth_dB = 10 * log10(Pr_bluetooth / 0.001);
% Plot the Receiver Power
plot(d_bluetooth, Pr_bluetooth_dB);
xlabel('Distance (m)');
ylabel('Received Power (dBm)');
title('Received Power vs Distance for Bluetooth');

snr_bluetooth = Pr_bluetooth / Pn; %signal noise ratio
snr_bluetooth_dB = 10 * log10(snr_bluetooth);
% Plot the SNR in dB against distance for Bluetooth
figure;
plot(d_bluetooth, snr_bluetooth_dB);
xlabel('Distance (m)');
ylabel('SNR (dB)');
title('SNR vs Distance for Bluetooth');

capacity_bluetooth = BW_bluetooth * log2(1 + snr_bluetooth); 
capacity_bluetooth_dB = 10 * log10(capacity_bluetooth);

% Plot the channel capacity in dB against distance for Bluetooth
figure;
plot(d_bluetooth, capacity_bluetooth_dB);
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('Channel Capacity vs Distance for Bluetooth');

%% CELLULAR SIMULATION

f_cellular = 850*1e6; %2G,GSM
BW_cellular = 200*1e3;
d_cellular = 100:100:5000;
P_t_cellular = 40;
lamb_cellular = c/f_cellular;

Pr_cellular = P_t_cellular * G_r * G_t * (lamb_cellular ./ (4 * pi * d_cellular)).^2; %received power
Pr_cellular_dB = 10 * log10(Pr_cellular / 0.001);
% Plot the Receiver Power for Cellular
figure;
plot(d_cellular, Pr_cellular_dB);
xlabel('Distance (m)');
ylabel('Received Power (dBm)');
title('Received Power vs Distance for Cellular');

snr_cellular = Pr_cellular / Pn; % signal noise ratio for cellular
snr_cellular_dB = 10 * log10(snr_cellular);
% Plot the SNR in dB against distance for Cellular
figure;
plot(d_cellular, snr_cellular_dB);
xlabel('Distance (m)');
ylabel('SNR (dB)');
title('SNR vs Distance for Cellular');

capacity_cellular = BW_cellular * log2(1 + snr_cellular); 
capacity_cellular_dB = 10 * log10(capacity_cellular);
% Plot the channel capacity in dB against distance for Cellular
figure;
plot(d_cellular, capacity_cellular_dB);
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('Channel Capacity vs Distance for Cellular');

%% COMPARITIVE ANALYSIS     
% Example for Received Power Comparison
figure;
semilogx(d_wifi, Pr_wifi_dB, 'r', 'LineWidth', 2); hold on;
semilogx(d_bluetooth, Pr_bluetooth_dB, 'b', 'LineWidth', 2);
semilogx(d_cellular, Pr_cellular_dB, 'g', 'LineWidth', 2);

grid on;
xlabel('Distance (m) - Log Scale');
ylabel('Received Power (dBm)');
legend('WiFi', 'Bluetooth', 'Cellular');
title('Technology Comparison: Received Power');

% Plot the SNR comparison
figure;
semilogx(d_wifi, snr_dB, 'r', 'LineWidth', 2); hold on;
semilogx(d_bluetooth, snr_bluetooth_dB, 'b', 'LineWidth', 2);
semilogx(d_cellular, snr_cellular_dB, 'g', 'LineWidth', 2);

grid on;
xlabel('Distance (m) - Log Scale');
ylabel('SNR (dB)');
legend('WiFi', 'Bluetooth', 'Cellular');
title('Technology Comparison: SNR');

% Plot the channel capacity comparison
figure;
semilogx(d_wifi, capacity_dB, 'r', 'LineWidth', 2); hold on;
semilogx(d_bluetooth, capacity_bluetooth_dB, 'b', 'LineWidth', 2);
semilogx(d_cellular, capacity_cellular_dB, 'g', 'LineWidth', 2);

grid on;
xlabel('Distance (m) - Log Scale');
ylabel('Channel Capacity (dB)');
legend('WiFi', 'Bluetooth', 'Cellular');
title('Technology Comparison: Channel Capacity');
