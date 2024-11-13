# Declaring both the lists
list1 = ["a", "b", "c", "d"]
list2 = ["a", "b"]

check = True
for e in list2:
    if e not in list1:
        check = False

if check == True:
    print("Elements of list2 exists in list1")
