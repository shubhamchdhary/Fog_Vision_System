""" Servoblaster from https://github.com/richardghirst/PiBits/tree/master/ServoBlaster 
Servo number   	   GPIO number	          Pin in P1 header
        0 		4 			P1-7 
	1 		17 			P1-11 
	2 		18 			P1-12 
	3 		21/27 			P1-13
	4 		22 			P1-15 
	5 		23 			P1-16 
	6 		24 			P1-18 
	7 		25 			P1-22

Change the /etc/init.d/servoblaster file to OPTS="--idle-timeout=2000 --pcm --p1pins=<list>" You can set 
the actual pin you want to dedicate to be servo with --p1pins option """

''' This is the modified code from github.com/tizianofiorenzani/ros_tutorials/blob/master/laser_scanner_tfmini/src/servoblaster.py '''

import time

class ServoBlaster():
	_servo_dict = { 4: 0, 17: 1, 18: 2, 21: 3, 22: 4, 23: 5, 24: 6, 25: 7}

	def __init__(self, gpio_port):
		self._gpio_port = gpio_port
		self._servo_number = self._servo_dict[gpio_port]

	def angle_to_dutyCycle(self,angle):
		self.angle = angle
		return (self.angle+45)/0.9

	def update(self,angle):
		self.dutyCycle = self.angle_to_dutyCycle(angle)
		servoStr = "%u=%u\n"  % (self._servo_number, self.dutyCycle)
		with open("/dev/servoblaster", "wb") as f:
			f.write(servoStr)

	def sweep(self,stepDelay):
		self.delay = stepdelay
		for i in range(0,180):
			self.update(i)
			time.sleep(self.delay)
		for i in range(180,0):
			self.update(i)
			time.sleep(self.delay)

	def slide(self,stepDelay,startAngle,endAngle):
		self.delay = stepDelay
		self.sAngle = startAngle
		self.eAngle = endAngle
		if self.sAngle < self.eAngle:
			for ii in range(self.sAngle,self.eAngle):
				step = (ii*0.055)+2
				self.pwm.ChangeDutyCycle(step)
				time.sleep(self.delay)
		elif self.sAngle > self.eAngle:
			for ii in range(self.sAngle,self.eAngle,-1):
				step = (ii*0.055)+2
				self.pwm.ChangeDutyCycle(step)
				time.sleep(self.delay)



if __name__ == "__main__":
	servo = ServoBlaster(18)
	servo.slide(60,120,0.05)
