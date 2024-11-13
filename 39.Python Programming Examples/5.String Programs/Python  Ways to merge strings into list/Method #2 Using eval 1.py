# Python code to merge all strings into a single list.

# Initialization of strings
str1 ="'Geeks', 'for', 'Geeks'"
str2 = "'121', '142'"
str3 ="'extend', 'India'"


out = [str1, str2, str3]

out = eval('+'.join(out))

# printing output
print(list(out))
