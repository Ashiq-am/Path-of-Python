a = ["apple", "banana", "kiwi", "cherry"]

# The key=len tells the sort() method
# to use length of each string during sorting
a.sort(key=len)
print(a)