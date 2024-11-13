# function to add facts
import randfacts as randfacts


def move():
	facts = randfacts.getFact(True)
	c = "*)"
	label = Label(root, text=c+facts)
	label.pack()
