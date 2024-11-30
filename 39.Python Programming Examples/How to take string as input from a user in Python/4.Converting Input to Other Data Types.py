age = input("Enter your age: ")

# Convert string to integer
#If the user enters something that is not a valid integer (e.g., a letter), it will raise a ValueError.

age = int(age)

print("In 10 years, you will be", age + 10, "years old.")