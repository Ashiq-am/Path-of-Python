# defining the 1st decorator
def decor1(func):
	print("_________________")

# defining the 2nd decorator
def decor2(func):
	print("$****************$")
	func()
	print("$****************$")

# using the decorator
@decor1
@decor2
def main():
	print("$ GeeksforGeeks $")

# Driver program to test the code
if __name__ == 'main':
	main()
