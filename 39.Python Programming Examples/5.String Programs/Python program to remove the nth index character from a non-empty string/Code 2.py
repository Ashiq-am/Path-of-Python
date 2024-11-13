# declaring a string variable
str = "Geeksforgeeks is fun."

# index to remove character at
n = 8

# extracts 0 to n-1th index
first_part = str[0:n]

# extracts characters from n+1th index until the end
second_part = str[n+1:]
print("Modified string after removing ", n, "th character ")

# combining both the parts together
print(first_part+second_part)
