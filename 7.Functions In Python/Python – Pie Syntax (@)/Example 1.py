# defining the decorator
def decor(func):
	print("#----------------#")
	func()
	print("#----------------#")

# using the decorator
@decor
def main():
	print("$ GeeksforGeeks $")

if __name__ == 'main':
	main()
