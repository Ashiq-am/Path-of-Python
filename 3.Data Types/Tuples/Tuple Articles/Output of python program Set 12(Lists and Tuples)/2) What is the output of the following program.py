L1 = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
val1, val2 = 0, ''
for x in L1:
	if(type(x) == int or type(x) == float):
		val1 += x
	elif(type(x) == str):
		val2 += x
	else:
		break
print(val1, val2)
