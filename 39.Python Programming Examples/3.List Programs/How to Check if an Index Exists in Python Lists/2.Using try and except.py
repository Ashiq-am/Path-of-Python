a = [10, 20, 30, 40]

try:
    print(a[5])
except IndexError:
    print("Index does not exist!")