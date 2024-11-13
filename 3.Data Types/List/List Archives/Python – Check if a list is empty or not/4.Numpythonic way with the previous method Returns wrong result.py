# Numpythonic way with the previous method
# Returns wrong result
import numpy


def Enquiry(lis1):
    return (numpy.array(lis1))


# Driver Code
lis1 = [0, ]
if Enquiry(lis1):
    print("Not Empty")
else:
    print("Empty")
