# Giving Input list and start-end
# index values
l = [2, 4, 5, 10]
i = 1
j = 3

# Loop starts
# Adding the previous values
# At every location
for x in range(len(l)):
	if(x == 0):
		continue
	else:
		l[x] = l[x]+l[x-1]

# Printing result
if(i == 0):
	print(l[j])
else:
	print(l[j]-l[i-1])
