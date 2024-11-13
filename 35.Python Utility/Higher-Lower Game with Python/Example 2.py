def assign():
	pass

def compare(p1, p2, user_input):
	pass

def play_higher_lower():
	pass


want_to_play = input("Do you want to play Higher Lower? (y/n)\n").lower()
if want_to_play == 'y':
	clear()
	play_higher_lower()
elif want_to_play == 'n':
	print("Program Exit Successful.")
else:
	print("Invalid Input, Program Exited.")
