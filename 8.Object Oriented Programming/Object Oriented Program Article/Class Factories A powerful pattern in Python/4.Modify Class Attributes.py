class Apple(object):
	color = 'red'

	@classmethod
	def classapple(cls):
		return cls.color


appleRed = Apple()
appleYellow = Apple()
appleGreen = Apple()

print("Apple Red: ", appleRed.classapple())

appleYellow.color = 'Yellow'
print("Apple Yellow: ", appleYellow.classapple())

appleGreen.color = 'Green'
print("Apple Green: ", appleGreen.classapple())
