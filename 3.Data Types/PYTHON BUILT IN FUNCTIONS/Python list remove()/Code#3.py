# Python3 program for practical application
# of removing 1 untill all 1 are removed from the list


list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]

# looping till all 1's are removed
while (list1.count(1)):
    list1.remove(1)

print(list1)
