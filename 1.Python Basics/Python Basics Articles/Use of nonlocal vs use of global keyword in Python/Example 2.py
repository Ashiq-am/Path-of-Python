def fun():
	var1 = 10

	def gun():
		# gun() initializes a new variable var1.
		var1 = 20
		print(var1, id(var1))

	print(var1, id(var1))
	gun()
fun()
