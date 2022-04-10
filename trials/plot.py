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
y_temp = []
y_diff = []
logData = []


index = count()




def animate(i):
	

	data = buffer.StreamBuffer(20)
	temp = data[-1][1]

	logData.append(temp)

	if len(logData) > 2:
		previousValue = logData[-2]
		lastValue = logData[-1]

		if previousValue != 0:

			diff = ((lastValue - previousValue) / previousValue) * 100
			y_diff.append(diff)
			print('change in percentage: %f ' %diff)

	

	# temp plot
	x_vals.append(next(index))
	y_temp.append(temp)





	ax.cla()
	ax.plot(x_vals, y_temp, label= 'Temperature')

	# plt.legend(loc='upper left')
	# plt.tight_layout



# define and adjust figure
fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
# ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
# ax1.set_facecolor('#DEDEDE')


s = serial.Serial('/dev/tty.usbserial-AK04OWDG', 250000)
ani = FuncAnimation(plt.gcf(), animate, interval = 500)

plt.tight_layout()
plt.show()




