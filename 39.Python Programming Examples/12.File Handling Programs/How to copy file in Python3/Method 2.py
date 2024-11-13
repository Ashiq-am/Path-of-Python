# open source file in read mode
source = open("c:\\SourceFolder\\gfg.txt", "r")

# open destination file in write mode
dest = open("c:\\DestinationFolder\\gfgcopy.txt", "w")

# read first line
line = source.readline()

# read lines until reached EOF
while line:

	# write line into destination file
	dest.write(line)
	# read another line
	line = source.readline()

# close both files
source.close()
dest.close()
