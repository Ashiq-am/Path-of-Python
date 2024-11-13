# Prompting the user for input
user_input = int(input())

# Splitting the input string into individual numbers
number_list = []

for i in range(user_input):
    number_list.append(int(input()))

# Printing the list of numbers
print("List of numbers:", number_list)
