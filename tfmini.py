import serial
import time

class Tfmini():

	def __init__(self,serialPort="/dev/ttyAMA0"):
		self.serialPort = serialPort
		self.ser = serial.Serial(serialPort,115200)
		if self.ser.is_open == False:
			self.ser.open()

# Receives data from tfmini.
	def getData(self):
		time0 = time.time()
		while True:
			count = self.ser.in_waiting
			if time.time()> time0 + 1: break
			if count > 8:
				recv = self.ser.read(9)
				self.ser.reset_input_buffer()
				if recv[0] == 'Y' and recv[1] == 'Y': # 0x59 is 'Y'
					low = int(recv[2].encode('hex'), 16)
					high = int(recv[3].encode('hex'), 16)
					distance = low + high * 256

#				if recv[0] == 0x59 and recv[1] == 0x59:     #python3
#					distance = recv[2] + recv[3] * 256
					return distance


if __name__ == '__main__':
#	t1 = time.time()
	tf = Tfmini()
#	t2 = time.time()
#	print(f'time in defining {t2-t1}')
	while True:
#		t3 = time.time()
#		print(f"Distance is: {tf.getData()} cm")
		print(tf.getData())
#		t4 = time.time()
#		print(f'time taken in getting data {t4-t3}')
