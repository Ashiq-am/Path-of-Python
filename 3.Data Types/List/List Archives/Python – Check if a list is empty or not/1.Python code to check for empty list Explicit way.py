# Python code to check for empty list
# Explicit way
def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1


# Driver Code
lis1 = []
if Enquiry(lis1):
    print("The list is not empty")
else:
    print("Empty List")
