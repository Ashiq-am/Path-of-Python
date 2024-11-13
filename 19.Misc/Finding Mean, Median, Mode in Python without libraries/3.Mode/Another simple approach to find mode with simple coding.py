# The list for which you need to find
# the Mode
y= [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8]

# First you sort it
# You will get numbers arranged from 3 to
# 11 in asc order
y.sort()

# Now open an empty list.
# What you are going to do is to count
# the occurrence of each number and append
# (or to add your findings to) L1
L1=[]

# You can iterate through the sorted list
# of numbers in y,
# counting the occurrence of each number,
# using the following code

i = 0
while i < len(y) :
	L1.append(y.count(y[i]))
	i += 1

# your L1 will be [1, 2, 2, 1, 3, 3, 3, 1, 3, 3, 3, 1],
# the occurrences for each number in sorted y

# now you can create a custom dictionary d1 for k : V
# where k = your values in sorted y
# and v = the occurrences of each value in y

# the Code is as follows

d1 = dict(zip(y, L1))

# your d1 will be {3: 1, 4: 2, 5: 1, 6: 3, 7: 1, 8: 3, 11: 1}
# now what you need to do is to filter
# the k values with the highest v values.
# do this with the following code

d2={k for (k,v) in d1.items() if v == max(L1) }

print("Mode(s) is/are :" + str(d2))
