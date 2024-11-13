# importing package
import turtle

# print distance (defalut)
print(turtle.distance())

for i in range(4):
    # draw one quadrent
    turtle.circle(50, 90)

    # print distance
    print(turtle.distance())
