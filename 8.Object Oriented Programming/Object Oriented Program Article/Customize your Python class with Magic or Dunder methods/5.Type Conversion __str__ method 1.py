class HelloClass(object):
	def __str__(self):
		return 'George'

print('Hello, % s' % HelloClass())
