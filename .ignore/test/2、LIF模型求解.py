import numpy as np
import matplotlib.pyplot as plt


def calc_next_step(Vm, I, step_t, remaining_refrac_time):
    Vl = -70
    Gl = 0.025
    C = 0.5
    if Vm > -50 and Vm < 0:  # threshold
        Vm = 30  # spike potential
    elif Vm > 0:
        Vm = -60  # reset potential
        remaining_refrac_time = remaining_refrac_time * 0 + 2  # reset everything to 2
    elif remaining_refrac_time > 0:
        Vm = -60  # reset potential
        remaining_refrac_time -= step_t
    else:
        Vm = Vm + step_t * (-Gl * (Vm - Vl) + I) / C
    if remaining_refrac_time < 0:
        remaining_refrac_time = remaining_refrac_time * 0
    return Vm, remaining_refrac_time


step_t = 0.01
t = np.arange(0, 200 + step_t, step_t)
Vm_out = np.zeros(np.shape(t)[0])
I = 0.9

ind = 0
Vm_out[0] = -70  # init state
remaining_refrac_time = 0
for tt in t[0:-1]:
    Vm_out[ind + 1], remaining_refrac_time = calc_next_step(Vm_out[ind], I, step_t, remaining_refrac_time)
    ind += 1
fig = plt.figure(figsize=(3.5,2.625))
plt.plot(t, Vm_out)
plt.xlabel("time /ms")
plt.ylabel("Memberance Potential /mV")
plt.show()
