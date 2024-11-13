import sys


print("the name of the program is ", sys.argv[0])

n = len(sys.argv[1])
a = sys.argv[1][1:n-1]
a = a.split(', ')

for i in a:
	print(i)
