# approach 2
# using stat function of os module
import os

file_size = os.stat('d:/file.jpg')
print("Size of file :", file_size.st_size, "bytes")
