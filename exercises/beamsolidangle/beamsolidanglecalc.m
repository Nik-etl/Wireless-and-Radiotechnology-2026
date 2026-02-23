clc;
close all;
clear all;
%%
% --- Input Section ---
tmin = input('The lower bound of theta in degree=');
tmax = input('The upper bound of theta in degree=');
pmin = input('The lower bound of phi in degree=');
pmax = input('The upper bound of phi in degree=');
%% 
% --- Coordinate and Step Assignments ---
% Convert degrees to radians immediately for integration
theta = (tmin:tmax) * (pi/180); 
phi = (pmin:pmax) * (pi/180);

% Assign step sizes (differential elements)
dth = theta(2) - theta(1);
dph = phi(2) - phi(1);

% Create grid for 2D patterns
[THETA, PHI] = meshgrid(theta, phi);

% --- Pattern Inputs ---
% Instruction asks to input field pattern E and assign as x
% Use 's' for string input if you want to evaluate it, or enter as code
x_str = input('The field pattern : E(THETA,PHI)=','s'); 
x = eval(x_str); % This will be cos(THETA) based on your requirements

v = input('The power pattern: P(THETA,PHI)=','s');
Pn = eval(v); % This will be cos(THETA).^2 based on your requirements

% --- Calculation of Beam Area (Prad) ---
% The beam solid angle is the integral of the normalized power pattern 
% over the sphere: Integral of [Pn(theta, phi) * sin(theta) dtheta dphi]
% We use the sum of the grid values multiplied by dth and dph (Numerical Integration)
Prad = sum(sum(Pn .* sin(THETA) * dth * dph));

% --- Formatting Output ---
fprintf('\n Input Parameters: \n-------------------- ');
fprintf('\n Theta =%2.0f', tmin);
fprintf(' : %2.0f', (tmax-tmin)/(length(theta)-1)); % Shows step in deg
fprintf(' : %2.0f', tmax);
fprintf('\n Phi =%2.0f', pmin);
fprintf(' : %2.0f', (pmax-pmin)/(length(phi)-1)); % Shows step in deg
fprintf(' : %2.0f', pmax);
fprintf('\n POWER PATTERN : %s', v);

fprintf('\n \n Output Parameters: \n-------------------- ');
% Printing the final Beam Area value
fprintf('\n BEAM AREA (steradians) = %3.2f\n', Prad);
