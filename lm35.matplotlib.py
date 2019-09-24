import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(1)

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(24, 26))

max_points = 10
# fill initial artist with nans (so nothing draws)
line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, 
                lw=2)

def init():
    return line,


def animate(i):
    rawString = arduino.readline()
    y = float(rawString.decode())  # I assume this 
    y = (1.1*y* 100)/1024

    print(y)

    old_y = line.get_ydata()  # grab current data
    new_y = np.r_[old_y[1:], y]  # stick new data on end of old data
    line.set_ydata(new_y)        # set the new ydata
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20,        blit=False)

plt.show()
