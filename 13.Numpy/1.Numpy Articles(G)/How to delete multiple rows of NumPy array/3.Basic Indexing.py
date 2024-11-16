import numpy as geek

# Defining the array
x = geek.arange(35).reshape(7, 5)

# Removing all rows before the 4th row
result = x[4:]
print(result)
