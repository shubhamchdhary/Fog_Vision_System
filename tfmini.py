import serial
import time

class Tfmini():
	#ser = serial.Serial("/dev/ttyAMA0", 115200)
	def __init__(self,serialPort="/dev/ttyAMA0"):
		self.serialPort = serialPort
		self.ser = serial.Serial(serialPort,115200)
		if self.ser.is_open == False:
			self.ser.open()
	def getData(self):
		#self.ser = serial.Serial(self.serialPort,self.baud)
		time0 = time.time()
		while True:
			count = self.ser.in_waiting
			if time.time()> time0 + 1: break
			if count > 8:
				recv = self.ser.read(9)
				self.ser.reset_input_buffer()
		#	if time.time()> time0 + 1: break
            # type(recv), 'str' in python2(recv[0] = 'Y'), 'bytes' in python3(recv[0] = 89)
            # type(recv[0]), 'str' in python2, 'int' in python3 

				if recv[0] == 0x59 and recv[1] == 0x59:     #python3
					distance = recv[2] + recv[3] * 256
				#strength = recv[4] + recv[5] * 256
				#print('(', distance, ',', strength, ')')
				#ser.reset_input_buffer()
					return distance

			#if recv[0] == 'Y' and recv[1] == 'Y':     #python2
			#	lowD = int(recv[2].encode('hex'), 16)      
			#	highD = int(recv[3].encode('hex'), 16)
			#	lowS = int(recv[4].encode('hex'), 16)      
			#	highS = int(recv[5].encode('hex'), 16)
			#	distance = lowD + highD * 256
			#	strength = lowS + highS * 256
			#	print(distance, strength)


if __name__ == '__main__':
	tf = Tfmini()
	print(tf.getData())

