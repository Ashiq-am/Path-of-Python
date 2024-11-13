import textwrap

wrapper = textwrap.TextWrapper(width=50)

s = '''\
	hello
	world
	'''
print(repr(s)) # prints ' hello\n	 world\n '

text = textwrap.dedent(s)
print(repr(text)) # prints 'hello\n world\n'
