# Opening a file in read mode
fp = open("example.txt", "r")

try:
	# Reading data from the file
	content = fp.read()
	print(content)
finally:
	# Closing the file to free up system resources
	fp.close()
