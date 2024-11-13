# ...

Race = False
if bet:
    Race = True
while Race:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            Race = False
            winning = turtle.pencolor()
            if winning == bet:
                print(
                    f"You have won! The {winning} turtle is the winner.")
            else:
                print(f"You lost! The {winning} turtle is the winner.")
                distance = random.randint(0, 10)
                turtle.forward(distance)
