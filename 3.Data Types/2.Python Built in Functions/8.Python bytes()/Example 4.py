# Python 3 code to demonstrate the
# working of bytes() on int, iterables, none

# initializing integer and iterables
a = 4
lis1 = [1, 2, 3, 4, 5]

# No argument case
print ("Byte conversion with no arguments : " + str(bytes()))

# conversion to bytes
print ("The integer conversion results in : " + str(bytes(a)))
print ("The iterable conversion results in : " + str(bytes(lis1)))
