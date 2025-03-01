import numpy as np
import matplotlib.pyplot as plt

# Define constants
tau_m = 5e-3  # Membrane time constant (s)
E_L = -70e-3  # Resting potential (V)
Delta_T = 1e-3  # Sharpness of initiation (V)
V_threshold = -50e-3  # Spike threshold (V)
R_m = 100e6  # Membrane resistance (ohm)
V_reset = -70e-3  # Reset voltage (V)
refractory_period = 0.8e-3  # Refractory period (s)

# Define simulation parameters
dt = 1e-4  # Time step (s)
simulation_time = 1.0  # Total simulation time (s)
time = np.arange(0, simulation_time, dt)

# Input current: Ornstein-Uhlenbeck process
mean_current = 40e-12  # Mean input current (A)
std_current = 120e-12  # Standard deviation of input current (A)
tau_ou = 3e-3  # OU process time constant (s)
I = np.zeros_like(time)
I[0] = mean_current
for t in range(1, len(time)):
    I[t] = I[t - 1] + dt / tau_ou * (mean_current - I[t - 1]) + np.sqrt(2 * dt / tau_ou) * std_current * np.random.randn()

# Initialize variables
V_m = np.ones_like(time) * E_L  # Membrane potential (V)
spike_times = []  # To store spike times
last_spike_time = -refractory_period

# Simulation loop
for t in range(1, len(time)):
    if time[t] - last_spike_time < refractory_period:
        # Refractory period: hold at reset potential
        V_m[t] = V_reset
    else:
        # Update membrane potential using EIF model
        dV_m = (E_L - V_m[t - 1] + Delta_T * np.exp((V_m[t - 1] - V_threshold) / Delta_T) + R_m * I[t - 1]) * (dt / tau_m)
        V_m[t] = V_m[t - 1] + dV_m

        # Check for spike
        if V_m[t] > V_threshold + 3 * Delta_T:
            V_m[t] = V_reset  # Reset potential
            last_spike_time = time[t]
            spike_times.append(time[t])

# Plot results
plt.figure(figsize=(10, 6))

# Plot membrane potential
plt.subplot(2, 1, 1)
plt.plot(time, V_m * 1e3, label="Membrane Potential (mV)")
plt.axhline((V_threshold + 3 * Delta_T) * 1e3, color='r', linestyle='--', label="Threshold")
plt.xlabel("Time (s)")
plt.ylabel("Membrane Potential (mV)")
plt.legend()
plt.title("EIF Model Simulation")

# Plot input current
plt.subplot(2, 1, 2)
plt.plot(time, I * 1e12, label="Input Current (pA)")
plt.xlabel("Time (s)")
plt.ylabel("Input Current (pA)")
plt.legend()

plt.tight_layout()
plt.show()
