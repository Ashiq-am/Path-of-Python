# Python Program to remove falsy values
# from List

# Function returning the updated list
def Remove_Falsy(List):
    List1 = []
    for i in List:
        if (bool(i)):
            List1.append(i)
    return List1


# Original List
List1 = [10, 20, 30, 0, False, 40, 0]
List2 = [False, None, 1, 2, 3, "Geeks"]
List3 = [[], (), "GeeksForGeeks", 26, 27]

# printing the updated list after removing Falsy values
print("List1[] = ", Remove_Falsy(List1))
print("List2[] = ", Remove_Falsy(List2))
print("List3[] = ", Remove_Falsy(List3))
