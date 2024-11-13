# Enter File Name with Extension
filename = "gfg.txt"

# Read file in binary mode
with open(filename, "rb") as file:
	# Command for Uploading the file "STOR filename"
	ftp_server.storbinary(f"STOR {filename}", file)
