#input Lists
list1=["gf","i","be"]
list2=["g","s","st"]

#List Comphrension
ans = [list1[i] + list2[i] for i in range(min(len(list1),len(list2)))]
print(ans)
