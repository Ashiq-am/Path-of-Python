# Collision
collision = isCollision(bullet_X, invader_X[i], bullet_Y, invader_Y[i])
if collision:
		score_val += 1
		bullet_Y = 600
		bullet_state = "rest"
		invader_X[i] = random.randint(64, 736)
		invader_Y[i] = random.randint(30, 200)
		invader_Xchange[i] *= -1
