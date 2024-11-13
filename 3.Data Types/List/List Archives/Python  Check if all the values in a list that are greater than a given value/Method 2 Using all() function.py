# python program to check if all
# values in the list are greater
# than val using all() function

def check(list1, val):
    return (all(x > val for x in list1))


# driver code
list1 = [10, 20, 30, 40, 50, 60]
val = 5
if (check(list1, val)):
    print("Yes")
else:
    print("No")

val = 20
if (check(list1, val)):
    print("Yes")
else:
    print("No")
