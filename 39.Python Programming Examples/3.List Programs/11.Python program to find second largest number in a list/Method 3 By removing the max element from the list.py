# Python program to find second largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# new_list is a set of list1
new_list = set(list1)

# removing the largest element from temp list
new_list.remove(max(new_list))

# elements in original list are not changed
# print(list1)

print(max(new_list))
