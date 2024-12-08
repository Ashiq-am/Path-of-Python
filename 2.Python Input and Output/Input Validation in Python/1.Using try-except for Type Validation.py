def func():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input!")

# Example usage
n = func()
print(n)