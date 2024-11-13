# Flick fidget spinner
def flick():
    # acceleration of spinner
    state['turn'] += 40


# setup window screen
setup(600, 400, 370, 0)
bgcolor("black")

tracer(False)
'''tracer brings back the fidget spinner into its initial state
after completing the rotation'''

# wing of fidget spinner
width(60)
color("orange")

# keyboard key for the rotation of spinner
onkey(flick, 'space')

listen()
animate()
done()
