# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake
# body
snake_body = [ [100, 50],
				[90, 50],
				[80, 50],
				[70, 50]
			]
# fruit posiiton
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# setting default snake direction
# towards right
direction = 'RIGHT'
change_to = direction
