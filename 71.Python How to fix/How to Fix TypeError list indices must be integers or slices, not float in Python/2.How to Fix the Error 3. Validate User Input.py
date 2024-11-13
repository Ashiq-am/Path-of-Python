my_list = [1, 2, 3, 4, 5]
user_input = input("Enter an index: ")  # Assume user enters 2.5
index = float(user_input)
if index.is_integer():
    print(my_list[int(index)])
else:
    print("Please enter a valid integer index.")
