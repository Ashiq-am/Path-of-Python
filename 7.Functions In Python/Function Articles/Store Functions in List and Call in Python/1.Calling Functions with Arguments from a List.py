def add(a, b):
  return a + b

#Stores the 'add' functions
operations = [add]

#calls function stored at index 0
#pass argumemts 10 and 5 to the 'add' function
result = operations[0](10, 5)
print("Addition:", result)