class Geeks:
	_website = "GeeksforGeeks"
	@property
	def website(self):
		return self._website
	@website.setter
	def website(self, value):
		self._website = value
# original value
obj = Geeks()
print("Original Value: " + obj.website)
# editing using property setter
obj.website = 'GFG'
print("Edited Value: " +obj.website)
