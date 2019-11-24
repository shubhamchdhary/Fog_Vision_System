import servo as sr

servo1 = sr.Servo(18)
servo1.start(50)
servo1.run(0,180,0.05)


