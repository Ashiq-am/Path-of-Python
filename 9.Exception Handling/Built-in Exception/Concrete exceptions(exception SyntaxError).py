try:
	print(eval('geeks for geeks'))
except SyntaxError, err:
	print('Syntax error %s (%s-%s): %s' % (err.filename, err.lineno, err.offset, err.text))
	print(err)
