""



'''
import matplotlib.pyplot as plt 
from matplotlib.patches import RegularPolygon 
import numpy as np 


coord = [[0, 0, 0], 
		[0, 1, -1], 
		[-1, 1, 0], 
		[-1, 0, 1], 
		[0, -1, 1], 
		[1, -1, 0], 
		[1, 0, -1]] 

colors = [["Green"], 
		["Green"], 
		["Green"], 
		["Green"], 
		["Green"], 
		["Green"], 
		["Green"]] 

labels = [['1'], ['2'], 
		['3'], ['4'], 
		['5'], ['6'], 
		['7']] 

# Horizontal cartesian coords 
hcoord =  for c in coord] 

# Vertical cartersian coords 
vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3.
		for c in coord] 

fig, ax = plt.subplots(1) 
ax.set_aspect('equal') 

# Add some coloured hexagons 
for x, y, c, l in zip(hcoord, vcoord, colors, labels): 
	
	# matplotlib understands lower 
	# case words for colours 
	color = c[0].lower() 
	hex = RegularPolygon((x, y), 
						numVertices = 6, 
						radius = 2. / 3., 
						orientation = np.radians(30), 
						facecolor = color, 
						alpha = 0.2, 
						edgecolor ='k') 
	
	ax.add_patch(hex) 
	
	# Also add a text label 
	ax.text(x, y + 0.2, l[0], ha ='center', 
			va ='center', size = 20) 

# add scatter points in hexagon centres 
ax.scatter(hcoord, vcoord, c =.lower() 
							for c in colors], 
		alpha = 0.5) 

plt.show() 




'''