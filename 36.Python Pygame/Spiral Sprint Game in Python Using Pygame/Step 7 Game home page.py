# if home_page bool is true that means its
# home page so show the game name and an
# animation clip of game and two buttons easy and hard
if home_page:
	connected.update()

	pygame.draw.circle(win, BLACK, CENTER, 80, 20)
	ball_group.update(color)
	# If easy button is clicked then only
	# one ball will revolve start=90degree
	if easy_btn.draw(win):
		ball_group.empty()
		ball = Balls((CENTER[0],
				CENTER[1]+RADIUS), RADIUS, 90, win)
		ball_group.add(ball)
		# Once the game is started turn
		# off the unnecessary booleans
		home_page = False
		game_page = True
		easy_level = True
	# If hard button is clicked then two balls
	# will revolve start=90degree and
	# 270degree respectively
	if hard_btn.draw(win):
		ball_group.empty()
		ball = Balls((CENTER[0],
				CENTER[1]+RADIUS), RADIUS, 90, win)
		ball_group.add(ball)
		ball = Balls((CENTER[0],
				CENTER[1]-RADIUS), RADIUS, 270, win)
		ball_group.add(ball)
		# Once the game is started turn off
		# the unnecessary booleans
		home_page = False
		game_page = True
		easy_level = False
