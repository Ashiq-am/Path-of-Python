# Python Code to convert ByteString key:value
# pair of dictionary to String.

# Initialising dictionary
x = {b'EmplId': b'12345', b'Name': b'Paras', b'Company': b'Cyware'}

# Initialising empty dictionary
y = {}

# Converting
for key, value in x.items():
	y[key.decode("utf-8")] = value.decode("utf-8")

# printing converted dictionary
print(y)
