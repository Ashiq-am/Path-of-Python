# Opening a file in write mode
fp = open("example.txt", "w")

try:
	# Writing data to the file
	fp.write("Hello, this is an example of file writing.")
finally:
	# Closing the file to free up system resources
	fp.close()
