# Update the score_page if its true then that
# means the game is over;
# So display the scores, home button, replay
# button, and sound button options for the user
if score_page:
		game_msg.update() # GAME
		over_msg.update() # OVER

		# Display score if boolean is onn else 0
		if score:
			final_score.update(score, color)
		else:
			final_score.update("0", color)
		# update the highscore if score is
		# greater than highscore
		if score and (score >= highscore):
			new_high_msg.update(shadow=False)

		# If home button is clicked then draw the
		# home_page window(win) and take care
		# of those extra booleans
		if home_btn.draw(win):
			home_page = True
			score_page = False
			game_page = False
			player_alive = True
			score = 0
			score_msg = Message(WIDTH//2, 100, 60, "0",
								score_font, (150, 150, 150), win)

		# If replay button is clicked then draw the game_page window(win) and take care of those extra booleans
		if replay_btn.draw(win):
			home_page = False
			score_page = False
			game_page = True
			score = 0
			score_msg = Message(WIDTH//2, 100, 60, "0",
						score_font, (150, 150, 150), win)
			# In game take easy or hard mode (users choice)
			if easy_level:
				ball = Balls((CENTER[0],
						CENTER[1]+RADIUS), RADIUS, 90, win)
				ball_group.add(ball)
			else:
				ball = Balls((CENTER[0],
						CENTER[1]+RADIUS), RADIUS, 90, win)
				ball_group.add(ball)
				ball = Balls((CENTER[0],
						CENTER[1]-RADIUS), RADIUS, 270, win)
				ball_group.add(ball)

			player_alive = True

		# Sound trigger points
		if sound_btn.draw(win):
			sound_on = not sound_on
			# Update the sound button image
			if sound_on:
				sound_btn.update_image(sound_on_img)
				pygame.mixer.music.play(loops=-1)
			else:
				sound_btn.update_image(sound_off_img)
				pygame.mixer.music.stop()
