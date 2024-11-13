from functools import reduce
numbers = list(range(1,6))
product= reduce(lambda x,y: x*y, numbers)
print(product)
