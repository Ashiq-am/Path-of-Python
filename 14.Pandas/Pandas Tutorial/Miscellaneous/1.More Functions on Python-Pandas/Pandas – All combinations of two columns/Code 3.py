# importing product
from itertools import product

# apply product method
print(list(product(df['gents'], df['ladies'])))
