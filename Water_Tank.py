import numpy as np
import matplotlib.pyplot as plt

water_level = 30
time_steps = 50
flow_rate = 5

target_level = 50
low_threshold = target_level - 10
high_threshold = target_level + 10

pump_on = False

controller_states = []
level_states = []

for t in range(time_steps):

    if t % 4 == 0:
        print(t)
        if water_level > target_level:
            pump_on = True
        elif water_level < target_level:
            pump_on = False
    else:
        # check the water level to turn controller on or off
        if water_level > high_threshold:
            pump_on = False
        elif water_level < low_threshold:
            pump_on = True

    # update the water level if controller is on
    if pump_on:
        water_level += flow_rate
    else:
        water_level -= flow_rate

    controller_states.append(pump_on)
    level_states.append(water_level)



plt.plot(level_states)
plt.xlabel("Timesteps")
plt.ylabel("Water Level")
plt.title("Water Tank Level")
plt.show()