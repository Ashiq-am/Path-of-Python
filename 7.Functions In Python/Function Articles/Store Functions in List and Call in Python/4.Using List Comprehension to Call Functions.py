def add(a, b):
  return a + b

# Create a list called 'operations' that stores
#the add and subtract functions
operations = [add]
results = [func(10, 5) for func in operations] # use list comprehension to call each function with arguments

print("Results:", results)