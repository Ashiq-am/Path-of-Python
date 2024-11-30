# Read input until the user stops
a = [i for i in iter(lambda: input("Enter an element (or press Enter to stop): "), "")]
print(a)