class gfg:
	vowels = ['a', 'e', 'i', 'o', 'u']

	# Function to reverse the list
	def __reversed__(self):
		return reversed(self.vowels)

# Main Function
if __name__ == '__main__':
	obj = gfg()
	print(list(reversed(obj)))
