# Python3 code to demonstrate
# to check if list is subset of other

# Importing
from collections import Counter


def checkInFirst(a, b):
    # getting count
    count_a = Counter(a)
    count_b = Counter(b)

    # checking if element exsists in second list
    for key in count_b:
        if key not in count_a:
            return False
        if count_b[key] > count_b[key]:
            return False
    return True


# initializing list
a = [1, 2, 4, 5]
b = [1, 2, 3]

# Calling function
res = checkInFirst(a, b)

# Printing list
print("Original list : " + str(a))
print("Original sub list : " + str(b))

if res == True:
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")


