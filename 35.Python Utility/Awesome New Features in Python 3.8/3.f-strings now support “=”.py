a = 5
b = 10

# Using = at the end of
# f-strings
print(f'{a + b = }')

# Using assignment operators
# inside f-strings
print(f'{(c := a + b)}')

print("The value of c:", c)
