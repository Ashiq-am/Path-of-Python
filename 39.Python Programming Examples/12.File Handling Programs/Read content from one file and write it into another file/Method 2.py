# Creating an output file in writing mode
output_file = open("gfg output file.txt", "w")

# Opening input file and scanning each line
# from input file and writing in output file
with open("gfg input file.txt", "r") as scan:
	output_file.write(scan.read())

# Closing the output file
output_file.close()
