# Python program to find second largest
# number in a list

# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

'''
# sort the list 
list1.sort()

# print second maximum element
print("Second largest element is:", list1[-2])

'''

# print second maximum element using sorted() method
print("Second largest element is:", sorted(list1)[-2])
