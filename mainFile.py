#This is the actual file for operating both the servos and tfmini.

#Yaw means lef-right motion and Pitch means up-down motion here.
import servo,tfmini,time
#import socket
from csv import writer

tf = tfmini.Tfmini()
yawServo = servo.Servo(16) #Attach yaw servo at pin 16.
yawServo.start(50) #Start pwm at 50 Hz.
pitchServo = servo.Servo(18) #Attach pitch servo at pin 18.
pitchServo.start(50)

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

step = 60  #Initial position of pitch control servo.
flag = 0   # Flag to check up or down motion. '0' for downward and '1' for upward.
lst = []

while True:
	if step == 120:     #Checking two extreme points of up-down motion.
		flag = 1
		saveData(['EOS'])  #EOS stands for End Of Scan.
	elif step == 60:
		flag = 0

	for ii in range(60,121):
#		t1 = time.time()
		distance = tf.getData()
#		t2 = time.time()
#		print(f'time taken by tf mini {t2-t1}')
		lst.append(str(distance))
#		sendData(str(distance))
		print(distance)
#		t3 = time.time()
		yawServo.goto(ii)
#		t4 = time.time()
#		print(f'time taken by servo {t4-t3}')
	saveData(lst)
	lst.clear()
#	sendData(lst)
	print('Left Sweep\n')

	if flag == 0:
		step += 10
	elif flag == 1:
		step -= 10
	pitchServo.goto(step)
	print('Pitch movement\n')

	if step == 120:
		flag = 1
		saveData(['EOF'])
	elif step == 60:
		flag = 0

	for ii in range(120,61,-1):
		distance = tf.getData()
		lst.append(str(distance))
#		sendData(str(distance))
		print(distance)
		yawServo.goto(ii)
	lst.reverse()
	saveData(lst)
	lst.clear()
	print('Right Sweep\n')

	if flag == 0:
		step += 10
	elif flag == 1:
		step -= 10

	pitchServo.goto(step)
	print("Pitch movement\n")
