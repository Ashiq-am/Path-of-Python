list1 = [23, 45, 65, 31, 1, 89]
list2 = [67, 89, 23, 45, 8, 90]

# Resultant list
ans = list1 + [data for data in list2 if data not in list1]

print("The resultant merged list is ")
print(ans)
