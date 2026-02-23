clc;
close all;
clear all;
%%

% --- Input Commands ---
tmin = input('The lower bound of theta in degree=');
tmax = input('The upper bound of theta in degree=');
pmin = input('The lower bound of phi in degree=');
pmax = input('The upper bound of phi in degree=');

% --- Assignment Section ---
tinc = 2;
pinc = 4;
rad = pi/180;

% --- Coordinate Conversions ---
theta1 = (tmin:tinc:tmax);
phi1 = (pmin:pinc:pmax);
theta = theta1 .* rad;
phi = phi1 .* rad;

% Meshgrid command to create a grid of spherical coordinates
[THETA, PHI] = meshgrid(theta, phi);

% --- Pattern Inputs ---
% For this task, enter 1 for both inputs when prompted
y1 = input('The field pattern: E(THETA,PHI)=');
v = input('The field pattern: P(THETA,PHI)=','s');

% Assign y as absolute value of y1
y = abs(y1);

% Note: ratio calculation provided in prompt snippet is incomplete,
% but y (the radius) is used directly in sph2cart for the plot.
[X, Y, Z] = sph2cart(PHI, (pi/2 - THETA), y);

% --- Plotting Section ---
mesh(X, Y, Z);
title('3 D Pattern', 'Color', 'b', 'FontName', 'Helvetica', 'FontSize', 12, 'FontWeight', 'demi');
axis equal; % Ensures the sphere doesn't look like an egg

% --- Output Formatting ---
fprintf('\n Input Parameters: \n-------------------- ');
fprintf('\n Theta =%2.0f', tmin);
fprintf(' : %2.0f', tinc);
fprintf(' : %2.0f', tmax);
fprintf('\n Phi =%2.0f', pmin);
fprintf(' : %2.0f', pinc);
fprintf(' : %2.0f', pmax);
fprintf('\n FIELD PATTERN : %s', v);
fprintf('\n \n Output is shown in the figure below----------- \n');
