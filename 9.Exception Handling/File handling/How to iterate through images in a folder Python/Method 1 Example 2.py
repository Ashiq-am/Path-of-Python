# import the modules
import os
from os import listdir

# get the path or directory
folder_dir = "C:/Users/RIJUSHREE/Desktop/Gfg images"
for images in os.listdir(folder_dir):

	# check if the image end swith png or jpg or jpeg
	if (images.endswith(".png") or images.endswith(".jpg")\
		or images.endswith(".jpeg")):
		# display
		print(images)
