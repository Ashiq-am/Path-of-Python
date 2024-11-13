# Enter File Name with Extension
filename = "gfg.txt"

# Write file in binary mode
with open(filename, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp_server.retrbinary(f"RETR {filename}", file.write)
