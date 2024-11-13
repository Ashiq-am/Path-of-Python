# Program for converting bytes to string using decode()
data = b'GeeksForGeeks'

# display input
print('\nInput:')
print(data)
print(type(data))

# converting
output = str(data, 'UTF-8')

# display output
print('\nOutput:')
print(output)
print(type(output))
