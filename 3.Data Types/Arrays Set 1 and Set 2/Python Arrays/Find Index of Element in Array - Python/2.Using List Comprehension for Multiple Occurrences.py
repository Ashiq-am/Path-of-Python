import array

arr = array.array('i', [10, 20, 30, 20, 50])

# Find all indices of 20
li = [i for i, x in enumerate(arr) if x == 20]
print(li)
