import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800,600

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("OrbitCatapult")

PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50
OBJ_SIZE = 5
VEL_SCALE = 100

BG = pygame.image.load("background.png")