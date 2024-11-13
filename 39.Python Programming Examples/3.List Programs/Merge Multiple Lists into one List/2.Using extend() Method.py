# Method - 2 : Using extend() method

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Merging the list
merged_list = []
merged_list.extend(list1)
merged_list.extend(list2)
merged_list.extend(list3)

print("The Merged list is")
print(merged_list)
