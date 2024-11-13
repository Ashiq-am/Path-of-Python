# some_module.py
class Listnode:
	pass

# main.py
from some_module import Listnode # Correct import statement

def main():
	node = Listnode() # No NameError now

if __name__ == "__main__":
	main()
