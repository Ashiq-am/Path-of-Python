def safe_concatenate(str1, str2, default="Guest"):
    return str1 + (str2 if str2 is not None else default)

my_string = "Hello, "
name = None

greeting = safe_concatenate(my_string, name)
print(greeting)  # Output: Hello, Guest
