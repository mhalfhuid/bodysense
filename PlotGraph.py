import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections

import serial, buffer
import SerialRead as sr

# initialise
y_temp = []
y_diff = []


# font type
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 20,
        }

# function to update the data
def my_function(i):
    # get data

    data = buffer.StreamBuffer(20)
    temp = data[-1][1]


    # cpu.popleft()
    # cpu.append(psutil.cpu_percent())

    # y_temp.popleft()
    y_temp.append(round(temp,1))

    if len(y_temp) >1:
        previousValue = y_temp[-2]
        lastValue = y_temp[-1]

        if previousValue != 0:

            diff = ((lastValue - previousValue) / previousValue) * 100
            y_diff.append(round(diff,2))
            # print('change in percentage: %f ' %diff)


    
    # clear axis
    ax.cla()
    ax1.cla()
    # plot cpu
    ax.plot(y_temp)
    ax.scatter(len(y_temp)-1, y_temp[-1])
    ax.text((len(y_temp)-1)/3, 35, "{}℃".format(y_temp[-1]), fontdict=font)

    # ax.text(len(y_temp)-1, y_temp[-1]+2, "{}℃".format(y_temp[-1]))
    ax.set_ylim(10,40)
   
    # plot memory
    if len(y_diff)>1:
        ax1.plot(y_diff)
        ax1.scatter(len(y_diff)-1, y_diff[-1])
        ax1.text(len(y_diff)-1, y_diff[-1]+2, "{}%".format(y_diff[-1]))
        ax1.set_ylim(-1,1)


    ax.title.set_text('Absolute Temperature')
    ax1.title.set_text('Temperature change')


# define and adjust figure
fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')


# animate
ani = FuncAnimation(fig, my_function, interval=500)
plt.tight_layout()
plt.show()