file_descriptors = []
for x in range(100000):
	file_descriptors.append(open('test.txt', 'w'))
