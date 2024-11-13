from os import popen

# Fileid of the file
fileid = "0x00000000000000000001000000000589"

# Running the command for obtaining the file path,
# of the file associated with the fileid
output = popen(fr"fsutil file queryfilenamebyid C:\ {fileid}").read()

print(output)
