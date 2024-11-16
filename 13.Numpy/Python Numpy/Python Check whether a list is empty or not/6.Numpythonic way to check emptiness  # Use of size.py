# Numpythonic way to check emptiness
# Use of size
import numpy


def Enquiry(lis1):
    return (numpy.array(lis1))


# Driver Code
lis1 = [0, ]
if Enquiry(lis1).size:
    print("Not Empty")
else:
    print("Empty")
