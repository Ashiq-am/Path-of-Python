# ...

colors = ["red", "orange", "yellow", "blue", "violet"]
X = -230
Y = -100
turtles = []
for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=Y + 50 * i)
    turtles.append(t)
