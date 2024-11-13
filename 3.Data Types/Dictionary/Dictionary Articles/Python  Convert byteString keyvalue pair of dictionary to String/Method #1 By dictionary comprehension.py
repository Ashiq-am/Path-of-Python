# Python Code to convert ByteString key:value
# pair of dictionary to String.

# Initialising dictionary
x = {b'EmplId': b'12345', b'Name': b'Paras', b'Company': b'Cyware'}

# Converting
x = { y.decode('ascii'): x.get(y).decode('ascii') for y in x.keys() }

# printing converted dictionary
print(x)
