# Open the binary file
file = open("string.bin", "rb")
# Reading the first three bytes from the binary file
data = file.read(3)
# Printing data by iterating with while loop
while data:
	print(data)
	data = file.read(3)
# Close the binary file
file.close()
