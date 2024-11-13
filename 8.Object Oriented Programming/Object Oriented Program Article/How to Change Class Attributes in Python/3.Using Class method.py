class Geeks:
	website = "GeeksforGeeks"
	@classmethod
	def update_website(cls, new_value):
		cls.website = new_value
# original value
print("Original Value: " + Geeks.website)
# editing using a class method
Geeks.update_website('GFG')
print("Edited Value: " +Geeks.website)
