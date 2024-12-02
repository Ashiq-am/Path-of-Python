s = "abc"
try:
    num = int(s)
    print(num)
except ValueError:
    print("Invalid input: cannot convert to integer")