# Fog Vision System

#servo.py
This file has a class defined for operating servos. It also has different methods for controlling servos.

#servoControl.py
This file has an example program to operate two servos by RPi simultaneously.

#myservoblaster.py
servoblaster library to operate servos.

#tfmini.py
This file has a class defined for operating Tfmini LIDAR module using RPi. It also has method defined in it for getting data from the LIDAR module. 

#mainFile.py
This file is the actual file used by the RPi to operate servos and tfmini together. It generates a file data.csv which contains distance data measured by the Tfmini which scanning.

#data.csv
This file contains distance data in comma separated values.  

#Lidar_view.py
Has program to read csv file and produce image from the point cloud data in it. 

Setup ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
![Screenshot](Lidar view new.PNG)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Output :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
![Screenshot](P_20200908_112324.jpg)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
