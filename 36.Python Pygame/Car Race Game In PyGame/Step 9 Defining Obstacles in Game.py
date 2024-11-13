# Loading the obstacles
def obstacle(obs_startx, obs_starty, obs):
	if obs == 0:
		obs_pic = pygame.image.load("car.jpg")
	elif obs == 1:
		obs_pic = pygame.image.load("car1.jpg")
	elif obs == 2:
		obs_pic = pygame.image.load("car2.jpg")
	elif obs == 3:
		obs_pic = pygame.image.load("car4.jpg")
	elif obs == 4:
		obs_pic = pygame.image.load("car5.jpg")
	elif obs == 5:
		obs_pic = pygame.image.load("car6.jpg")
	elif obs == 6:
		obs_pic = pygame.image.load("car7.jpg")
	gamedisplays.blit(obs_pic, (obs_startx, obs_starty))
