# Ball Class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx, self.posy = posx, posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac, self.yFac = 1, 1

        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    # Used to display the object on the screen
    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    # Used to update the state of the object
    def update(self):
        self.posx += self.xFac * self.speed
        self.posy += self.yFac * self.speed

        # Reflecting the ball if it touches either of the vertical edges
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xFac *= -1

        # Reflection from the top most edge of the screen
        if self.posy <= 0:
            self.yFac *= -1

        # If the ball touches the bottom most edge of the screen, True value is returned
        if self.posy >= HEIGHT:
            return True

        return False

    # Resets the position of the ball
    def reset(self):
        self.posx = 0
        self.posy = HEIGHT
        self.xFac, self.yFac = 1, -1

    # Used to change the direction along Y axis
    def hit(self):
        self.yFac *= -1

    # Returns the rect of the ball. In this case, it is the ball itself
    def getRect(self):
        return self.ball
