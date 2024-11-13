# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# removes elements from index 1 to 4
# i.e. 5, 17, 18, 23 will be deleted
del list1[1:5]

print(*list1)
