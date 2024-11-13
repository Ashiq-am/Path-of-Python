list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Converting the list into set
set1 = set(list1)
set2 = set(list2)

# find the union of the sets and converting resultant set to list
ans = list(set1.union(set2))

print("The resultant merged list is ")
print(ans)
