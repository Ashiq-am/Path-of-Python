class sample:

	# constructor overloading
	# based on args
	def __init__(self, *args):

		# if args are more than 1
		# sum of args
		if len(args) > 1:
			self.ans = 0
			for i in args:
				self.ans += i

		# if arg is an integer
		# square the arg
		elif isinstance(args[0], int):
			self.ans = args[0]*args[0]

		# if arg is string
		# Print with hello
		elif isinstance(args[0], str):
			self.ans = "Hello! "+args[0]+"."


s1 = sample(1, 2, 3, 4, 5)
print("Sum of list :", s1.ans)

s2 = sample(5)
print("Square of int :", s2.ans)

s3 = sample("GeeksforGeeks")
print("String :", s3.ans)
