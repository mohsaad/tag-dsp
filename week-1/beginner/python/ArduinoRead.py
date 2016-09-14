# Mohammad Saad
# 9/13/2016
# TAG-DSP
# ArduinoRead.py
# A script to read values passed over a serial connection 
# from an Arduino.

import serial

'''
For Windows, your port is likely COM3 or COM4, passed in as a string.

If you're on linux, use dmesg | grep tty to find out where it's attached, 
likely /dev/ttyUSB0 or /dev/ttyUSB1.

Baudrate defines the speed of our connection, or how fast we send data through
the connection. If the baudrates do not match, you won't understand the data at all.

When we run this, it opens the port for writing or reading to the Arduino.
'''
s = serial.Serial('COM3', baudrate = 9600)

'''
Now, we can read lines from the Arduino. Remember that we just wanted to print out the 
current value of the brightness of the LED. So that's what's going to show up here.

We set up a loop to just print the first 1000 values.
'''
for i in range(0, 1000):
	print(s.readline())

'''
Finally, close the port! Two programs on the device can't read from the serial port at the same time,
because that would cause synchronization issues in case one program wanted to read and the other
wanted to write.

close() allows us to close our connection and free up the device for other programs to access.
'''
s.close()