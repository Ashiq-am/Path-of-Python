# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg

try:
	raise Networkerror("Error")

except Networkerror as e:
	print (e.args)
