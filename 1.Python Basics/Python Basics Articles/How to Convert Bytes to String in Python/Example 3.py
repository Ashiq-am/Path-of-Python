# Program for converting bytes to string using decode()

# import required module
import codecs

data = b'GeeksForGeeks'

# display input
print('\nInput:')
print(data)
print(type(data))

# converting
output = codecs.decode(data)

# display output
print('\nOutput:')
print(output)
print(type(output))
