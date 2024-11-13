# some_module.py
class Listnode:
	pass

# main.py
# Incorrect: Missing import statement
# from some_module import Listnode

def main():
	node = Listnode() # Raises NameError

if __name__ == "__main__":
	main()
