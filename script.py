import serial, time


print ('\n\nPYSERIAL\n')

sPort = '/dev/cu.usbmodem14101'           #On Mac - find this using >ls /dev/cu.usb*

arduino = serial.Serial(sPort, 9600, timeout=.1)


while True:
    time.sleep(1)  # give the connection a second to settle
    arduino.write("Hello ")
    data = arduino.readline()
    if data:
		print data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason