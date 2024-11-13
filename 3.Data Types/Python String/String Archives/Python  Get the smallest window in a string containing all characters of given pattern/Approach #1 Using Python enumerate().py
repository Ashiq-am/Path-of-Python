string = 'new string'
pattern = 'rg'

# let's find the index of r and g in String and the
# stor them in index list (index[])
index=[]
for x in range(len(pattern)):
	if pattern[x] in string:
		index.append(string.index(pattern[x]))

# sorting the r and g index's
index.sort()

# save first index in l
l = len(index)
low = int(index[0])

# save last index in h
high = int(index[l-1])
h = high +1
for i in range(low,h):
	print(string[i],end=" ")
