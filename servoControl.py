import servo as sr

ser1 = sr.Servo(16)
ser1.start(50)
ser2 = sr.Servo(18)
ser2.start(50)

step = 0
flag = 0 # Flag to check up or down motion. 0 for downward and 1 for upward.

while True:
	ser1.slide(0,240,0.05)
	if flag == 0:
		step += 15
	elif flag == 1:
		step -= 15
	ser2.goto(step)

	ser1.slide(240,0,0.05)
	if flag == 0:
		step += 15
	elif flag == 1:
		step -= 15
	ser2.goto(step)

	if step == 180:
		flag = 1
	elif step == 0:
		flag = 0
