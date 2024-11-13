def init(self, color):
	self.color = color


def getColor(self):
	return self.color


Apple = type('Apple', (object,), {
	'__init__': init,
	'getColor': getColor,
})

appleRed = Apple(color='red')
print(appleRed.getColor())
