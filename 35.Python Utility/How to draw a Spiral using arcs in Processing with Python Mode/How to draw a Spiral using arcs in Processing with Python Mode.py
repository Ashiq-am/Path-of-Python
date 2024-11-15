# function to setup size of
# output window
def setup():
    # to set background color of window
    # to black color
    background(0)

    # to set width and height of window
    # to 1000px and 1000px respectively
    size(1000, 1000)


# function to draw on the window
def draw():
    # to set the fill color of the arcs to None
    noFill()

    # to set the border color of arcs to white
    # that is rgb(255,255,255)
    stroke(255, 255, 255)

    # loop to create 16 arcs
    for i in range(16):
        # if i is even
        if i % 2 == 0:

            # function to create an arc with center (500,525)
            # and width and height as 50px and 50px respectively
            # In each alternate iteration, the height and width of
            # the arcs increases by 100px. The arc starts at
            # 90 degrees that is half times PI and end at 270
            # degrees (90 + 180) that is PI + half times PI
            arc(500, 525, 50 + i * 50, 50 + i * 50, HALF_PI, HALF_PI + PI)

        # if i is odd
        else:
            # function to create an arc with center (500,500)
            # and width and height as 50px and 50px respectively
            # In each alternate iteration, the height and width of
            # the arcs increases by 100px. The arc starts at
            # 270 degrees that is PI + half times PI and end at 450
            # degrees (90 + 360) that is 2 times PI + half times PI
            arc(500, 500, 50 + i * 50, 50 + i * 50, HALF_PI + PI, HALF_PI + 2 * PI)
