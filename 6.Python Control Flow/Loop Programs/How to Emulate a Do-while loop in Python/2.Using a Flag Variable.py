# Example list of strings
strings_list = ["geeksforgeeks", "C++", "Java", "Python", "C", "MachineLearning"]

print("Strings in the list:")

# Using a while loop with a flag variable
flag = True
index = 0
while flag:

    # Execute the code block at least once
    current_string = strings_list[index]
    print(current_string)

    # Increment the index
    index += 1

    # Set the flag to False if the loop should terminate
    if index >= len(strings_list):
        flag = False

# Code block outside the loop
print("Loop has exited.")
