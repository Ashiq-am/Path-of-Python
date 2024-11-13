import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")

FPS = 60
clock = pygame.time.Clock()
run = True
