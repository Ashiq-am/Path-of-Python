# input Lists
list1 = ["gf", "i", "be"]
list2 = ["g", "s", "st"]

# defining the resultanat list
ans = []

# iterating through each elements of both the lists
for i in range(0, min(len(list1), len(list2))):
    ans.append(list1[i] + list2[i])

# Output
print(ans)
