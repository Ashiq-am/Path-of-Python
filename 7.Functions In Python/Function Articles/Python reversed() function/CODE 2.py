vowels = ['a', 'e', 'i', 'o', 'u']

# Function to reverse the list
def __reversed__(self):
	return reversed(self.vowels)

# Main Function
if __name__ == '__main__':
	print(list(reversed(vowels)))
