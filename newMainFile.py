#This is the actual file for operating both the servos and tfmini.

#Yaw means lef-right motion and Pitch means up-down motion here.
import myservoblaster,tfmini,time
#import socket
from csv import writer

tf = tfmini.Tfmini()
yawServo = myservoblaster.ServoBlaster(17) #Attachs yaw servo at pin 16.
pitchServo = myservoblaster.ServoBlaster(18) #Attachs pitch servo at pin 18.

#sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Starts server.
#sc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#sc.bind((socket.gethostname(),1234))
#sc.listen(4)

def saveData(data): #Saves data in a csv file. Argument 'data' is a list.
	with open('data.csv','a') as f:
		csvW = writer(f)
		csvW.writerow(data)


#def sendData(data):
#	ti = time.time()
#	sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Starts server.
#	sc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#	sc.bind(('127.0.0.1',1234))
#	sc.listen(4)
#	clientSocket,address = sc.accept()
#	print(f"Connetion with {address} established.")
#	clientSocket.send(bytes(data,"utf-8"))
#	sc.shutdown(socket.SHUT_WR)
#	sc.close()
#	tj = time.time()
#	print(f'time taken in data sending {tj-ti}')


step = 60  # Initial position of pitch control servo.
flag = 0   # Flag to check 'up' or 'down' motion. '0' for downward and '1' for upward.
lst = []
stepDelay = 0.001  #step delay of yawServo
inr = 10   # Increament in step of pitch servo. Modify this variable to increase or decrease rows of data.csv

while True:
	if step == 120:     #Checking two extreme points of up-down motion.
		flag = 1
		saveData(['EOS'])  #EOS stands for End Of Scan.
	elif step == 60:
		flag = 0

	for ii in range(60,120):
		distance = tf.getData()
		lst.append(str(distance))
#		sendData(str(distance))
		print(distance)
		yawServo.update(ii)
		time.sleep(stepDelay)
	saveData(lst)
	del lst[:]
#	sendData(lst)
	print('Left Sweep\n')

	if flag == 0:
		step += inr
	elif flag == 1:
		step -= inr

	pitchServo.update(step)
	print('Pitch movement\n')

	if step == 120:
		flag = 1
		saveData(['EOS'])
	elif step == 60:
		flag = 0

	for ii in range(120,61,-1):
		distance = tf.getData()
		lst.append(str(distance))
#		sendData(str(distance))
		print(distance)
		yawServo.update(ii)
		time.sleep(stepDelay)
	lst.reverse()
	saveData(lst)
	del lst[:]
	print('Right Sweep\n')

	if flag == 0:
		step += inr
	elif flag == 1:
		step -= inr
	pitchServo.update(step)
	print("Pitch movement\n")
