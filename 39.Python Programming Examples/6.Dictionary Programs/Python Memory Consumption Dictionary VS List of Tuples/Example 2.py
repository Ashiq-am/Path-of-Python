import sys

# for dict
dict = {(1, "G"), (2, "F"), (3, "G")}
print(dict)
print(sys.getsizeof(dict))

# for list of tuples
list1 = (1, 2, 3)
list2 = ("G", "F", "G")
LoT = list(zip(list1, list2))
print(LoT)
print(sys.getsizeof(LoT))
