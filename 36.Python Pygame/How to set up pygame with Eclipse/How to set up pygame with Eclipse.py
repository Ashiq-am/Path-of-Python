# code
import pygame
import math
import random
from pygame.locals import *


class Player():
	def __init__(self):
		self.rect = pygame.draw.rect(screen, (0, 0, 255),
									(30, 30, 60, 60))
		self.dist = 20

	def handle_keys(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				exit()
			elif e.type == KEYDOWN:
				key = e.key
				if key == K_LEFT:
					self.draw_rect(-5, 0)
				elif key == K_RIGHT:
					self.draw_rect(5, 0)
				elif key == K_UP:
					self.draw_rect(0, -5)
				elif key == K_DOWN:
					self.draw_rect(0, 5)
				elif key == K_ESCAPE:
					pygame.quit()
					exit()

	def draw_rect(self, x, y):
		screen.fill((0, 0, 0))
		self.rect = self.rect.move(x*self.dist, y*self.dist)
		pygame.draw.rect(screen, (0, 255, 255), self.rect)
		pygame.display.update()

	def draw(self, surface):
		pygame.draw.rect(screen, (0, 255, 255),
						(30, 30, 60, 60))


pygame.init() # initializing pygame

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("MOVE THE BLOCK OVER THE WINDOW")
clock = pygame.time.Clock()

player = Player()
screen.fill((0, 0, 0))
player.draw(screen)
pygame.display.update()

while True:
	player.handle_keys()
