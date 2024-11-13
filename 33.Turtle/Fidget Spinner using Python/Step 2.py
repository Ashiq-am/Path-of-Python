# Animate fidget spinner
def animate():
	if state['turn'] > 0:
		state['turn'] -= 1

	spin()
	ontimer(animate, 20)
