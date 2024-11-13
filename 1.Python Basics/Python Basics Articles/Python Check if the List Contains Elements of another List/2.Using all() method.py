# Declaring both the lists
list1 = ["a", "b", "c", "d"]
list2 = ["a", "b"]

check = all(e in list1 for e in list2)

if check == True:
    print("Elements of list2 exists in list1")
