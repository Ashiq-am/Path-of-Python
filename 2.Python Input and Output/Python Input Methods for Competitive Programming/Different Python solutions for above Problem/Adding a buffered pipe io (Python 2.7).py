# template begins
#####################################

# import libraries for input/ output handling
# on generic level
import atexit, io, sys

# A stream implementation using an in-memory bytes
# buffer. It inherits BufferedIOBase.
buffer = io.BytesIO()
sys.stdout = buffer

# print via here
@atexit.register
def write():
	sys.__stdout__.write(buffer.getvalue())

#####################################
# template ends

# normal method followed
# input N
n = int(raw_input())

# input the array
arr = [int(x) for x in raw_input().split()]

# initialize variable
summation = 0

# calculate sum
for x in arr:
	summation += x

# print answer
print(summation)








"""While handling a large amount of data usually, the normal method fails to execute within the time limit. 
Method 2 helps in maintaining a large amount of I/O data. Method 3 is the fastest. 
Usually, handling of input data files greater than 2 or 3 MBs is helped via method 2 and 3.

Note : above mention codes are in Python 2.7, to use in Python 3.X versions. Simply replace the raw_input() 
with Python 3.X’s input() syntax. Rest should work fine."""