# Python program to check if all values
# in the list are less than given value

# Function to check the value
def CheckForLess(list1, val):
    # traverse in the list
    for x in list1:

        # compare with all the
        # values with value
        if val <= x:
            return False
    return True


# Driver code
list1 = [11, 22, 33, 44, 55]
val = 65
if (CheckForLess(list1, val)):
    print("Yes")
else:
    print("No")
