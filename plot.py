# plots

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import serial, buffer
import SerialRead as sr


plt.style.use('fivethirtyeight')


x_vals = []
y_vals = []


index = count()

def animate(i):
	

	data = buffer.StreamBuffer(20)
	temp = data[-1][1]

	x_vals.append(next(index))
	y_vals.append(temp)



	plt.cla()
	plt.plot(x_vals, y_vals, label= 'Temperature')

	plt.legend(loc='upper left')
	plt.tight_layout



s = serial.Serial('/dev/tty.usbserial-AK04OWDG', 250000)
ani = FuncAnimation(plt.gcf(), animate, interval = 500)

plt.tight_layout()
plt.show()




