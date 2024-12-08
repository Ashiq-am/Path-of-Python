import array

arr = array.array('i', [10, 20, 30, 40, 50])
first_two, *rest = arr[:2], arr[2:]
print(first_two)  # [10, 20]
print(rest)       # [30, 40, 50]