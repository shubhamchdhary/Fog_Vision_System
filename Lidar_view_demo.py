# This is a Python file to display point cloud data from csv file obtained from LIDAR.
# Author Shubham Chaudhary, Shuarya Pandey and Mohit Yadav.

try:
	import os,time
	import matplotlib as mpl
	import matplotlib.pyplot as plt
	#from mpl_toolkits.mplot3d import Axes3D as a3d
	import numpy as np
	from shutil import copyfile
	#from pyntcloud import PyntCloud as pc
except:
	print('Required modules not found. Needs to have matplotlib and numpy installed')
else:
	file1 = 'data.csv'
	file2 = 'data2.csv'													  # Name of the csv file
	[height, width] = [8,7] 												  # Dimension of figure window
	lowerThreshold = 0														  # Lower limit of z-axis
	upperThreshold = 1200													  # Upper limit of z-axis
	rows,columns = 12,60

	mpl.rcParams['toolbar'] = 'None'                      					  # Hides toolbar from plot 
	#mpl.rcParams['figure.facecolor'] = 'k' 

	#arr = np.genfromtxt(file,delimiter=',')  
	#print(arr)

	while os.path.exists('finished.txt') != True:
		print('Holding for sync....')
		time.sleep(0.00001)
	os.remove('finished.txt')
	#copyfile(file1,file2)

	while True:
		try:
			arr = np.genfromtxt(file1,delimiter=',')     						  # Loads csv file
			#print(arr)
		except:
			print('csv file not found. Please check the current working directory. Or check if the file the correct.')
		else:
			if arr.shape[0] == rows or arr.shape[1] == columns: 
				zn = np.flip(arr,axis=0)											  # Inverting array vertically to match scan data with inveted y-axis
				y = np.array([i for i in range(0,arr.shape[0])])
				x = np.array([i for i in range(0,arr.shape[1])])

				for ii,index in enumerate(0,arr.shape[0]+1):										# Iterates the rows of file
					z = arr[int(arr.shape[0]/2)]										# Taking mid-scan value of vertical scans
					if index == arr.shape[0]:                    				    # Checks for the character 'EOS' in the csv file

						# Following 8 lines are for syncing csv data
						with open('sync.txt','w') as f:
							print('sync.txt created')
							f.close()
							#print(f1.closed)
						os.remove(file1)
						#os.remove(file2)
						time.sleep(0.0002)

					else:
						# Plotting 
						plt.figure('LIDAR View',figsize=(height, width))

						####################################### Top view plot ######################################################################
			#			fig2 = plt.figure('top')
						plt.subplot(211)
						plt.title('Top View', fontweight ="bold")
						plt.axis([0,arr.shape[1],lowerThreshold,upperThreshold])   	          					# Sets axes limits 
						plt.plot(x,z,'bo')                       							# Creates plot
						plt.ylabel('Distance from Vehicle in cms')
						plt.xlabel('Vehicle side')
						plt.grid(True)                            						 	# Toggles grid
						plt.draw()                                 						    # Shows plot

						####################################### Front view plot ####################################################################
			#			fig1 = plt.figure('front view')
						plt.subplot(212)
						plt.title('Front View', fontweight ="bold")
						plt.xlabel('Width')
						plt.ylabel('Height')
						plt.pcolormesh(x,y,zn,cmap="gray_r",vmin=lowerThreshold,vmax=upperThreshold,shading='auto')
						cbar = plt.colorbar()
						cbar.set_label('Distance from Vehicle in cms', rotation=270,labelpad=12)
						plt.tight_layout()
						plt.draw()
						plt.pause(0.00001)													# Pause for a while. Argument is in second
						plt.clf()															# Clears plot in the figure window 

			else:
				os.remove(file1)


