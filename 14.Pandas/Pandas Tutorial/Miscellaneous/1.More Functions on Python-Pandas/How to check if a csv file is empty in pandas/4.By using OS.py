import os

file_size = os.path.getsize('/content/data_2.csv') # Find the size of csv file

if file_size == 0:	 # if size is empty
	print('File is Empty')
else:
	# proceed with reading the file
	with open('/content/data_2.csv', 'r') as read:
		lines = read.readlines()
		print(lines)
