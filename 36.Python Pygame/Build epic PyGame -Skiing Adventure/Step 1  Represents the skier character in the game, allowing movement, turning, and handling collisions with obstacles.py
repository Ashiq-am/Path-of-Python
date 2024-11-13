import sys

import cfg
import pygame
import random
import os

class SkierClass(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# Initialize the skier's attributes
		self.direction = 0
		# Paths to skier's images for different directions
		self.imagepaths = cfg.SKIER_IMAGE_PATHS[:-1]
		# Load the skier's image
		self.image = pygame.image.load(self.imagepaths[self.direction])
		self.rect = self.image.get_rect()
		# Set the initial position of the skier
		self.rect.center = [320, 100]
		# Skier's speed (x, y)
		self.speed = [self.direction, 6 - abs(self.direction) * 2]
		self.flag_count = 0
		self.score = 0

	def turn(self, num):
		self.direction += num
		# Limit the direction to -2 (left) as minimum
		self.direction = max(-2, self.direction)
		# Limit the direction to 2 (right) as maximum
		self.direction = min(2, self.direction)
		center = self.rect.center
		self.image = pygame.image.load(self.imagepaths[self.direction])
		self.rect = self.image.get_rect()
		self.rect.center = center
		# Update the skier's speed based on the new direction
		self.speed = [self.direction, 6 - abs(self.direction) * 2]
		return self.speed

	def move(self):
		self.rect.centerx += self.speed[0]
		self.rect.centerx = max(20, self.rect.centerx)
		# Limit the skier's position to the left edge of the screen
		self.rect.centerx = min(620, self.rect.centerx)
		# Limit the skier's position to the right edge of the screen

	def setFall(self):
		# Set the skier's image to the falling image when the skier hits an obstacle (tree or stone)
		self.image = pygame.image.load(cfg.SKIER_IMAGE_PATHS[-1])

	def setForward(self):
		# Set the skier's image to the forward image after the skier recovers from a fall
		self.direction = 0
		self.image = pygame.image.load(self.imagepaths[self.direction])


# The code continues with other classes and functions
