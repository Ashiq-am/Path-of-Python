# basic method of input output
# input N
from click._compat import raw_input

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
