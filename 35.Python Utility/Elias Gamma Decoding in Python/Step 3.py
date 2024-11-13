# Converting binary to integer
for i in range(len(x)):
	if x[i] == '1':
		n = n+math.pow(2, i)
return int(n)
