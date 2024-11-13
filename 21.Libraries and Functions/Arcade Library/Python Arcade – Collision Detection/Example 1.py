# Importing arcade module
import arcade

# Creating MainGame class
class MainGame(arcade.Window):
	def __init__(self):
		super().__init__(600, 600, title="Player Movement")

		# Initializing a variable to store
		# the velocity of Player1 and Player2
		self.vel_x1 = 380
		self.vel_x2 = 380

		self.scene = None

		# Creating variable to store player sprite
		self.player1 = None

		# Creating variable to store player sprite
		self.player2 = None

	# Creating on_draw() function to draw on the screen
	def on_draw(self):
		arcade.start_render()

		# Drawing the scene
		self.scene.draw()

	def setup(self):

		# Creating scene
		self.scene = arcade.Scene()

		# Adding player sprite
		self.player_sprite1 = arcade.Sprite("Player.png", 1)
		self.player_sprite2 = arcade.Sprite("Player2.png", 1)

		# Adding coordinates for the center of the sprite
		self.player_sprite1.center_x = 20
		self.player_sprite1.center_y = 300

		# Adding coordinates for the center of the sprite
		self.player_sprite2.center_x = 580
		self.player_sprite2.center_y = 300

		# Adding sprites in scene
		self.scene.add_sprite('Player', self.player_sprite1)
		self.scene.add_sprite('Player', self.player_sprite2)

	# Creating on_update function to
	# update the x coordinate
	def on_update(self, delta_time):

		# Changing x coordinate of players
		self.player_sprite1.center_x += self.vel_x1 * delta_time
		self.player_sprite2.center_x -= self.vel_x2 * delta_time

		# Checking if sprites are colliding or not
		colliding = arcade.check_for_collision(
			self.player_sprite1, self.player_sprite2)

		# If sprites are colliding then changing direction
		if colliding:
			self.vel_x1 *= -1
			self.vel_x2 *= -1

		# Changing the direction if sprites crosses the scren boundary
		if self.player_sprite1.center_x > 600 or self.player_sprite1.center_x < 0:
			self.vel_x1 *= -1

		if self.player_sprite2.center_x > 600 or self.player_sprite2.center_x < 0:
			self.vel_x2 *= -1


# Calling MainGame class
game = MainGame()
game.setup()
arcade.run()
