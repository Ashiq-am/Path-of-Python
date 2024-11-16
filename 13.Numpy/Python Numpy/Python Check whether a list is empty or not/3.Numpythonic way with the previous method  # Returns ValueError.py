# Numpythonic way with the previous method
# Returns ValueError
import numpy


def Enquiry(lis1):
    return (numpy.array(lis1))


# Driver Code
lis1 = [0, 1]
if Enquiry(lis1):
    print("Not Empty")
else:
    print("Empty")
