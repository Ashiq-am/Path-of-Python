def fun(num):
	try:
		r = 1/num
	except:
		print('Exception raies')
		return
	return r

print(fun(10))
print(fun(0))
