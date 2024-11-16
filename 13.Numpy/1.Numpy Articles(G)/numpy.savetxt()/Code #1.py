# Python program explaining
# savetxt() function
import numpy as geek

x = geek.arange(0, 10, 1)
print("x is:")
print(x)

# X is an array
c = geek.savetxt('geekfile.txt', x, delimiter =', ')
a = open("geekfile.txt", 'r')# open file in read mode

print("the file contains:")
print(a.read())
