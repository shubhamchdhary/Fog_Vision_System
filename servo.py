'''Class to run servo motor.'''

import RPi.GPIO as gpio
import time

class Servo():

# Configures servoPin as output pin for servo.
	def __init__(self,servoPin):
		self.servoPin = servoPin
		gpio.setwarnings(False)
		gpio.setmode(gpio.BCM)
		gpio.setup(self.servoPin,gpio.OUT)

# Starts pwm for servo control at servoPin.
	def start(self,pwmFreq):
		self.pwmFreq = int(pwmFreq)
		self.pwm = gpio.PWM(self.servoPin,self.pwmFreq)
		self.pwm.start(1)

# Sends servo rotor to specified angle.
	def goto(self,angle):
		self.duty = (angle*0.055)+2           #duty represents steps.
		self.pwm.ChangeDutyCycle(self.duty)

# Continuously runs servo between two angles.
	def sweep(self,startAngle,endAngle,stepDelay): #Angle in degree from 2 to 180.
		self.sAngle = startAngle
		self.eAngle = endAngle
		self.delay = stepDelay
		for i in range(self.sAngle,self.eAngle):
			step = (i*0.055)+2
			self.pwm.ChangeDutyCycle(step)
			time.sleep(self.delay)
		for j in range(self.eAngle,self.sAngle,-1):
			step = (j*0.055)+2
			self.pwm.ChangeDutyCycle(step)
			time.sleep(self.delay)


# Moves a servo once between defined positions.
	def slide(self,startAngle,endAngle,stepDelay):
		self.sAngle = startAngle
		self.eAngle = endAngle
		self.delay = stepDelay
		for ii in range(self.sStep,self.eStep):
			step = (ii*0.055)+2
			self.pwm.ChangeDutyCycle(step)
			time.sleep(self.delay)


if __name__ == "__main__":
	servo1 = Servo(18)
	servo1.start(60)
	servo1.sweep(60,120,0.05)

