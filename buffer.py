import serial 
import SerialRead as sr
import time



def StreamBuffer(datapoints):
	s = serial.Serial('/dev/tty.usbserial-AK04OWDG', 250000)
	buffer = []
	for i in range(datapoints):
	    
	    data = sr.SensorDataReader(s)
	    if data is None:
	    	pass
	    else:
	    	temp = data[0]
	    	buffer.append((i,temp))
	    
	    i+=1

	s.close()

	return buffer

# test
# for i in range(100):
# 	data = StreamBuffer(20)
# 	print(data[-1][1])
# 	i+=1
# 	time.sleep(0.2)
