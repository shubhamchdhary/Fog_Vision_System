# Fog Vision System
This project aims at developing a system capable of providing a view of forthcoming objects to an automobile driver in foggy or unclear weather condition and even at night. The project uses LIDAR (Tf Mini Plus with 850nm IR Light) as its main sensor for fog penetration and Raspberry Pi 3B+ as the computing unit. 

More details available in Project Report : https://drive.google.com/file/d/1vYBo0ckk718FwpUBV0SaPBexlutJoTjd/view?usp=sharing

**servo.py**\
This file has a class defined for operating servos. It also has different methods for controlling servos.

**servoControl.py**\
This file has an example program to operate two servos by RPi simultaneously.

**myservoblaster.py**\
servoblaster library to operate servos.

**tfmini.py**\
This file has a class defined for operating Tfmini LIDAR module using RPi. It also has method defined in it for getting data from the LIDAR module. 

**mainFile.py**\
This file is the actual file used by the RPi to operate servos and tfmini together. It generates a file data.csv which contains distance data measured by the Tfmini which scanning.

**data.csv**\
This file contains distance data in comma separated values.  

**Lidar_view.py\**
Has program to read csv file and produce image from the point cloud data in it. 

Interaction between Scanning Program (mainFile.py) and Plotting Program(Lidar_view.py)\
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
![alt text](https://github.com/shubhamchaudharybrg/Fog_Vision_System/blob/3fec3c44644f564389e287f406caa6f43b919315/Images/Block%20Diagram.PNG)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Setup \
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
![alt text](https://github.com/shubhamchaudharybrg/Fog_Vision_System/blob/3fec3c44644f564389e287f406caa6f43b919315/Images/Setup.jpg)    
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Output \
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
![alt text](https://github.com/shubhamchaudharybrg/Fog_Vision_System/blob/40acf57a99479cf8d9a307c48cf162b7070b403a/Images/Lidar%20view%20new.PNG?raw=true)
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
