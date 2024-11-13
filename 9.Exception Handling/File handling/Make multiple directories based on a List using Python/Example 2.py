import os

root_path = 'Documents/tmp/year/month/week/day/hour'

list = ['car', 'truck', 'bike', 'cycle', 'train']

for items in list:
	path = os.path.join(root_path, items)
	os.mkdir(path)
