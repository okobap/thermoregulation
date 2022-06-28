import time

import matplotlib.pyplot as plt
import numpy as np

def update_line(line1, new_x, new_y):
    line1.set_xdata(np.append(line1.get_xdata(),[new_x]))
    line1.set_ydata(np.append(line1.get_ydata(),[new_y]))
    
    # Rescale axes limits
    ax.relim()
    ax.autoscale()

    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(0.1)


x = [0]
y = [0]

plt.ion()

ax: plt.Axes
figure, ax = plt.subplots(figsize=(10, 8))
(line1,) = ax.plot(x, y)
ax.autoscale(True)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

for i in range(100):
    new_y = np.sin(i) 
    new_x = i
    update_line(line1, new_x, new_y)


















