""""""



'''In addition to that, two more functions _next_() and _iter_() make the generator function more 
compact and reliable.
 
Example :'''



# Python code to illustrate generator, yield() and next().
def generator():
	t = 1
	print('First result is ',t)
	yield t

	t += 1
	print('Second result is ',t)
	yield t

	t += 1
	print('Third result is ',t)
	yield t

call = generator()
next(call)
next(call)
next(call)
