class snowfall(arcade.Window):
    def __init__(self, width, height, title):
        # Calls "__init__" of parent class
        # (arcade.Window) to setup screen
        super().__init__(width, height, title)

    def start_snowfall(self):
        # Set up snowfall and initialize variables.
        self.snowfall_list = []

        for i in range(50):
            # Create snowfall instance
            snowfall = snow_fall()

            # Randomly position snowfall
            snowfall.x = random.randrange(Width)
            snowfall.y = random.randrange(Height + 200)

            # Set other variables for the snowfall
            snowfall.size = random.randrange(8)
            snowfall.speed = random.randrange(20, 40)
            snowfall.angle = random.uniform(math.pi, math.pi * 2)

            # Add snowflake to snowfall list
            self.snowfall_list.append(snowfall)
