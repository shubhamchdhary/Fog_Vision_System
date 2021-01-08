# This is a Python file to display point cloud data from csv file obtained from LIDAR.
# Author Shubham Chaudhary, Shuarya Pandey and Mohit Yadav.

try:
	import os,time
	import matplotlib as mpl
	import matplotlib.pyplot as plt
	#from mpl_toolkits.mplot3d import Axes3D as a3d
	import numpy as np
	
except:
	print('Required modules not found. Needs to have matplotlib and numpy installed')
else:
	file = 'data.csv'					  # Name of the csv file
	[height, width] = [8,7] 				  # Dimension of figure window
	lowerThreshold = 0					  # Lower limit of z-axis
	upperThreshold = 1200					  # Upper limit of z-axis
	rows,columns = 20,120

	mpl.rcParams['toolbar'] = 'None'        		  # Hides toolbar from plot 
	#mpl.rcParams['figure.facecolor'] = 'k'

	while True:
		
		# Following 4 lines holds program untill new scan completes
		while os.path.exists('EOS.txt') != True:	    # EOS -> End Of Scan
			print('Plotter holding for sync....')
			#time.sleep(0.0000001)
		os.remove('EOS.txt')
		
		try:
			arr = np.genfromtxt(file,delimiter=',')     # Loads csv file
			#print(arr)
		except:
			print('csv file not found. Please check the current working directory. Or check if the file the correct.')
		else:
			if arr.shape[0] == rows or arr.shape[1] == columns:
				zn = np.flip(arr,axis=0)       	    # Inverting array vertically to match scan data with inveted y-axis
				y = np.array([i for i in range(0,arr.shape[0])])
				x = np.array([i for i in range(0,arr.shape[1])])
				z = arr[int(arr.shape[0]/2)]

				# Plotting
				plt.figure('LIDAR View',figsize=(height, width))

				####################################### Top view plot ######################################################################
			#	fig2 = plt.figure('top')
				plt.subplot(211)
				plt.title('Top View', fontweight ="bold")
				plt.axis([0,arr.shape[1],lowerThreshold,upperThreshold])   	        # Sets axes limits 
				plt.plot(x,z,'bo')                       				# Creates plot
				plt.ylabel('Distance from Vehicle in cms')
				plt.xlabel('Vehicle side')
				plt.grid(True)                            			 	# Toggles grid
				plt.draw()                    						# Shows plot

				####################################### Front view plot ####################################################################
			#	fig1 = plt.figure('front view')
				plt.subplot(212)
				plt.title('Front View', fontweight ="bold")
				plt.xlabel('Width')
				plt.ylabel('Height')
				plt.pcolormesh(x,y,zn,cmap="gray_r",vmin=lowerThreshold,vmax=upperThreshold,shading='auto')
				cbar = plt.colorbar()
				cbar.set_label('Distance from Vehicle in cms', rotation=270,labelpad=12)
				plt.tight_layout()
				plt.draw()
				plt.pause(0.00001)							# Pause for a while. Argument is in second
				plt.clf()
				
				# Following 5 lines are for syncing with data from pi.
				with open('COP.txt','w') as f:						# COP -> Completion Of Plot
					print('COP.txt created')
					f.close()
				os.remove(file)
				#time.sleep(0.0002)
				
			else:
				os.remove(file)

