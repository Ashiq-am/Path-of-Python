list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Resultant list
ans = []

# Traversing the list item one by one
for data in list1:
    if data not in ans:
        ans.append(data)

for data in list2:
    if data not in ans:
        ans.append(data)

print("The resultant merged list is ")
print(ans)
