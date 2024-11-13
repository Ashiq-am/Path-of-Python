# on Screen UI
def background():
	gamedisplays.blit(backgroundpic, (0, 0))
	gamedisplays.blit(backgroundpic, (0, 200))
	gamedisplays.blit(backgroundpic, (0, 400))
	gamedisplays.blit(backgroundpic, (700, 0))
	gamedisplays.blit(backgroundpic, (700, 200))
	gamedisplays.blit(backgroundpic, (700, 400))
	gamedisplays.blit(yellow_strip, (400, 0))
	gamedisplays.blit(yellow_strip, (400, 100))
	gamedisplays.blit(yellow_strip, (400, 200))
	gamedisplays.blit(yellow_strip, (400, 300))
	gamedisplays.blit(yellow_strip, (400, 400))
	gamedisplays.blit(yellow_strip, (400, 500))
	gamedisplays.blit(strip, (120, 0))
	gamedisplays.blit(strip, (120, 100))
	gamedisplays.blit(strip, (120, 200))
	gamedisplays.blit(strip, (680, 0))
	gamedisplays.blit(strip, (680, 100))
	gamedisplays.blit(strip, (680, 200))


def car(x, y):
	gamedisplays.blit(carimg, (x, y))
