''



'''
# inside the gaming Loop 

	# bouncing the ball 
	if ball_X + ballPixel >= width or ball_X <= 0: 
		ball_XChange *= -1
	if ball_Y + ballPixel >= height or ball_Y <= 0: 
		ball_YChange *= -1

	# moving the ball 
	ball_X += ball_XChange 
	ball_Y += ball_YChange 


'''