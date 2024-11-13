file_descriptors = []
for x in range(100000):
	file_descriptors.append(open('test.txt', 'w'))









'''An error message saying that too many files are open. The above example is a case of file 
descriptor leakage. It happens because there are too many open files and they are not closed. 
There might be chances where a programmer may forget to close an opened file.'''





