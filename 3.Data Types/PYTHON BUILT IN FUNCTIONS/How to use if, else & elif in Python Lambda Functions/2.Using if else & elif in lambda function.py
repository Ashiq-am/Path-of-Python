# Use if-else in Lambda Functions

# check if two numbe is qual or greater or lesser
result = lambda x,y : f"{x} is smaller than {y}" \
    if x < y else (f"{x} is greater than {y}" if x > y
               else f"{x} is equal to {y}")


# print for numbers
print(result(12, 11))
print(result(12, 12))
print(result(12, 13))
