# Python code to sort a list by creating
# another list Use of sorted()
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2


# Driver code
lst = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
print(Sorting(lst))
