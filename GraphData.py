import serial 
import SerialRead as sr
import time



def StreamBuffer(datapoints):
	s = serial.Serial('/dev/tty.usbserial-AK04OWDG', 250000)
	buffer = []
	for i in range(datapoints):
	    
	    data = sr.SensorDataReader(s)
	    if isinstance(data[0], float):
	    	temp = data[0]
	    	buffer.append((i,temp))
	    else:
	    	pass
	    
	    i+=1

	s.close()

	return buffer


for i in range(100):
	data = StreamBuffer(50)
	print(data[-1])
	i+=1
	time.sleep(0.5)
