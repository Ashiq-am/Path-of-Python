class Apple(object):
	color = 'red'

	@classmethod
	def classapple(cls):
		return cls.color


def create_Apple_subclass(new_color):
	class SubApple(Apple):
		color = new_color
	return SubApple


sappleYellow = create_Apple_subclass('Yellow')
print("Apple Color: ", sappleYellow.classapple())

sappleGreen = create_Apple_subclass('Green')
print("Apple Color: ", sappleGreen.classapple())
