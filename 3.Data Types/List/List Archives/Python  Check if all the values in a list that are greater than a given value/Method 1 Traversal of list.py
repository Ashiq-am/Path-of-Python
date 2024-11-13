# python program to check if all
# values in the list are greater
# than val using traversal

def check(list1, val):
    # traverse in the list
    for x in list1:

        # compare with all the values
        # with val
        if val >= x:
            return False
    return True


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
