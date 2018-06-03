%% initial condition
R = 1e3;
C = 1e-6;
syms omega;
%% normal plot
fplot(log10(omega), 20 * log10(sqrt((R^2 * C^2 * omega^2)/(1 + R^2 * C^2 * omega^2))), [0.001, 100000])
hold on
fplot(20 * log10(1))
fplot(20 * log10(0.0000001))
hold off
%% end of file