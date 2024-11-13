# function to get the coordinates of states.
# click on the point you want to display
# state name and then the x and y
# coordinates will be printed in console
def print_xy(x, y):
	print(f"{x}, {y}")


# onscreenclick is an event listenrer
# that calls a function everytime we
# click on screen.
screen.onscreenclick(print_xy)
