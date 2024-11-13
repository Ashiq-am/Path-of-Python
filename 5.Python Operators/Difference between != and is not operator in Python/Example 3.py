# Python3 code to
# illustrate the
# difference between
# != and is not operator
# [] is an empty list
list1 = []
list2 = []
list3 = list1

# First if
if (list1 != list2):
    print(" First if Condition True")
else:
    print("First else Condition False")

# Second if
if (list1 is not list2):
    print("Second if Condition True")
else:
    print("Second else Condition False")

# Third if
if (list1 is not list3):
    print("Third if Condition True")
else:
    print("Third else Condition False")

list3 = list3 + list2

# Fourth if
if (list1 is not list3):
    print("Fourth if Condition True")
else:
    print("Fourth else Condition False")
