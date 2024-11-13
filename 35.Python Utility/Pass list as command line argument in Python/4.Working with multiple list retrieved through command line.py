import sys


print ("the name of the program is ", sys.argv[0])

n = len(sys.argv[1])
a = sys.argv[1][1:n-1]
a = a.split(', ')

A = [int(i) for i in a]
b = 0

for i in A:
	b += i
print("sum of all the list members is ", b)

n = len(sys.argv[2])
c = sys.argv[2][1:n-1]
c = c.split(', ')

d = ""

for i in c:
	d = d+i

print ("sum of all the list members is ", d)
