# Fuction to set up size of output window
# and colour mode.
def setup():
    size(600, 600)
    colorMode(HSB)
    noStroke()


# Function to set up colour fill and ellise size.
def draw():
    fill(0x11000000)
    fill(0x1000000)
    fill(0x11000011)

    rect(0, 0, width, height)
    fill(frameCount % 255, 255, 255)
    ellipse(random(0, width), random(0, height), 40, 40)
