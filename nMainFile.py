# This is the actual file for operating both the servos and tfmini.
# Author Shubham Chaudhary, Shaurya Pandey and Mohit Yadav

# Yaw means lef-right motion and Pitch means up-down motion here.
import myservoblaster,tfmini,time,os
from csv import writer
import numpy as np

tf = tfmini.Tfmini()
yawServo = myservoblaster.ServoBlaster(17) #Attachs yaw servo at GPIO pin 17.
pitchServo = myservoblaster.ServoBlaster(18) #Attachs pitch servo at GPIO pin 18.

def saveData(data): #Saves data in a csv file. Argument 'data' is a list.
	with open('data.csv','a') as f:
		csvW = writer(f)
		csvW.writerow(data)
		f.close()

step = 60  # Initial position of pitch control servo.
flag = 0   # Flag to check 'up' or 'down' motion. '0' for downward and '1' for upward.
lst = []
stepDelay = 0.001  #step delay of yawServo
inr = 3   # Increament in step of pitch servo. Modify this variable to increase or decrease rows of data.csv
l = list(np.arange(60,120,0.5))

while True:

	if step < 120:
		yawServo.update(60)
		pitchServo.update(60)
		for ii in l:
			t1 = time.time()
			distance = tf.getData()
			t2 = time.time()
			t = t2-t1
			print('time taken is ')
			print(t)
			if distance == 0:
				distance = 1200
			lst.append(str(distance))
#			sendData(str(distance))
			print(distance)
			yawServo.update(ii)
#			time.sleep(stepDelay)
		lst.reverse()
		saveData(lst)
#		del lst[:]
		l.reverse()
#		sendData(lst)
		print('Left Sweep\n')

		pitchServo.update(step)
		print('Pitch movement\n')
		step += inr

		for ii in l:
			#distance = tf.getData()
			#lst.append(str(distance))
#			sendData(str(distance))
			#print(distance)
			yawServo.update(ii)
			time.sleep(stepDelay)
		#lst.reverse()
		saveData(lst)
		del lst[:]
		l.reverse()
		print('Right Sweep\n')

		pitchServo.update(step)
		print("Pitch movement\n")
		step += inr

	elif step == 120:
		step = 60
		with open('EOS.txt','w') as f:
			print('EOS.txt created')
			f.close()
		while os.path.exists('COP.txt') != True:
			print('Holding for sync....')
			time.sleep(0.0001)
		os.remove('COP.txt')
		yawServo.update(60)
		pitchServo.update(60)
