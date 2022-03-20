import serial 
import SerialRead as sr

s = serial.Serial('/dev/tty.usbserial-AK04OWDG', 250000)
for i in range(1000):
    
    print(sr.SensorDataReader(s))
    i+=1

s.close()