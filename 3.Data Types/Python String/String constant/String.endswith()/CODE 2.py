# Python code shows the working of
# .endswith() function

text = "geeks for geeks."

# start parameter: 10
result = text.endswith('geeks.', 10)
print(result)

# Both start and end is provided
# start: 10, end: 15
# Returns False
result = text.endswith('geeks', 10, 15)
print(result)

# returns True
result = text.endswith('geeks', 10, 14)
print(result)
