# import package
import turtle

# start recording polygon
turtle.begin_poly()

# form an ellipse
turtle.circle(20,90)
turtle.circle(10,90)
turtle.circle(20,90)
turtle.circle(10,90)

# end recording polygon
turtle.end_poly()

# get poly that recorded
print(turtle.get_poly())
