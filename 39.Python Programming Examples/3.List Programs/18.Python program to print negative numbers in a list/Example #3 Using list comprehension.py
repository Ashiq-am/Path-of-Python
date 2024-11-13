# Python program to print negative Numbers in a List

# list of numbers
list1 = [-10, -21, -4, 45, -66, 93]

# using list comprehension
neg_nos = [num for num in list1 if num < 0]

print("Negative numbers in the list: ", *neg_nos)
