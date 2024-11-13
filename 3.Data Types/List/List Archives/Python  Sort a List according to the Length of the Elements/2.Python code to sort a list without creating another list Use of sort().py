# Python code to sort a list without
# creating another list Use of sort()
def Sorting(lst):
    lst.sort(key=len)
    return lst


# Driver code
lst = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
print(Sorting(lst))
