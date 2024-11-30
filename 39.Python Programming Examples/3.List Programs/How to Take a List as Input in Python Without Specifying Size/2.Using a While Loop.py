# Initialize an empty list
a = []

print("Enter elements (press Enter without typing to stop):")
while True:
    val = input("Enter an element (or press Enter to finish): ")
    if val == "":
        break  # Exit loop when user presses Enter without typing
    a.append(el)

print(a)