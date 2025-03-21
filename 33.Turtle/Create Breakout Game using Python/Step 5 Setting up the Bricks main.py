import turtle as tr
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time

screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()

playing_game = True


screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)

def check_collision_with_walls():

	global ball, score, playing_game, ui

	# detect collision with left and right walls:
	if ball.xcor() < -580 or ball.xcor() > 570:
		ball.bounce(x_bounce=True, y_bounce=False)
		return

	# detect collision with upper wall
	if ball.ycor() > 270:
		ball.bounce(x_bounce=False, y_bounce=True)
		return

	# detect collision with bottom wall
	# In this case, user failed to hit
	# the ball thus he loses. The game resets.
	if ball.ycor() < -280:
		ball.reset()
		return

def check_collision_with_paddle():

	global ball, paddle
	# record x-axis coordinates of ball and paddle
	paddle_x = paddle.xcor()
	ball_x = ball.xcor()

	# check if ball's distance(from its middle)
	# from paddle(from its middle) is less than
	# width of paddle and ball is belo a certain
	# coordinate to detect their collision
	if ball.distance(paddle) < 110 and ball.ycor() < -250:

		# If Paddle is on Right of Screen
		if paddle_x > 0:
			if ball_x > paddle_x:
				# If ball hits paddles left side it
				# should go back to left
				ball.bounce(x_bounce=True, y_bounce=True)
				return
			else:
				ball.bounce(x_bounce=False, y_bounce=True)
				return

		# If Paddle is left of Screen
		elif paddle_x < 0:
			if ball_x < paddle_x:
				# If ball hits paddles left side it
				# should go back to left
				ball.bounce(x_bounce=True, y_bounce=True)
				return
			else:
				ball.bounce(x_bounce=False, y_bounce=True)
				return

		# Else Paddle is in the Middle horizontally
		else:
			if ball_x > paddle_x:
				ball.bounce(x_bounce=True, y_bounce=True)
				return
			elif ball_x < paddle_x:
				ball.bounce(x_bounce=True, y_bounce=True)
				return
			else:
				ball.bounce(x_bounce=False, y_bounce=True)
				return

def check_collision_with_bricks():
	global ball, bricks

	for brick in bricks.bricks:
		if ball.distance(brick) < 40:
			brick.quantity -= 1
			if brick.quantity == 0:
				brick.clear()
				brick.goto(3000, 3000)
				bricks.bricks.remove(brick)

			# detect collision from left
			if ball.xcor() < brick.left_wall:
				ball.bounce(x_bounce=True, y_bounce=False)

			# detect collision from right
			elif ball.xcor() > brick.right_wall:
				ball.bounce(x_bounce=True, y_bounce=False)

			# detect collision from bottom
			elif ball.ycor() < brick.bottom_wall:
				ball.bounce(x_bounce=False, y_bounce=True)

			# detect collision from top
			elif ball.ycor() > brick.upper_wall:
				ball.bounce(x_bounce=False, y_bounce=True)

while playing_game:
	screen.update()
	time.sleep(0.01)
	ball.move()

	check_collision_with_walls()

	check_collision_with_paddle()

	check_collision_with_bricks()

tr.mainloop()
