my_variable = None
if some_condition:
    my_variable = "Hello"
result = (my_variable or "Default") + " World"
print(result)  # Output: Default World (if some_condition is False)
