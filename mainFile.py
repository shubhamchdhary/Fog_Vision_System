#This is the actual file for operating both the servos and tfmini.

import servo
import tfmini
import time

servo1 = servo.Servo(16)
servo1.start(50)
servo2 = servo.Servo(18)
servo2.start(50)

step = 0
flag = 0 # Flag to check up or down motion. 0 for downward and 1 for upward.

while True:
	if step == 100: #Checking two extreme points of updown motion.
		flag = 1
	elif step == 0:
		flag = 0

	servo1.slide(60,180,0.1)
	if flag == 0:
		step += 15
	elif flag == 1:
		step -= 15
	time.sleep(10)
	servo2.goto(step)
	time.sleep(10)

	if step == 100:
		flag = 1
	elif step == 0:
		flag = 0

	servo1.slide(180,60,0.1)
	if flag == 0:
		step += 15
	elif flag == 1:
		step -= 15
	time.sleep(10)
	servo2.goto(step)
	time.sleep(10)
