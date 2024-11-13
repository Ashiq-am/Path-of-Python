def create_apple_class():
	def init(self, color):
		self.color = color

	def getColor(self):
		return self.color

	return type('Apple', (object,), {
		'__init__': init,
		'getColor': getColor,
	})


Apple = create_apple_class()
appleObj = Apple('red')
print(appleObj.getColor())
