# movement of the invader
for i in range(no_of_invaders):

		if invader_Y[i] >= 450:
			if abs(player_X-invader_X[i]) < 80:
				for j in range(no_of_invaders):
					invader_Y[j] = 2000
					explosion_sound = mixer.Sound('data/explosion.wav')
					explosion_sound.play()
				game_over()
				break
