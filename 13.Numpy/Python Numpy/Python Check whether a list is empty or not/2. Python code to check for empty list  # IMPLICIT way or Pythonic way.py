# Python code to check for empty list
# IMPLICIT way or Pythonic way
def Enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0


# Driver Code
lis1 = []
if Enquiry(lis1):
    print("The list is Empty")
else:
    print("The list is not empty")
