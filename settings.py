import pygame
import random
import ctypes
randomInit = random.randint(0, 0)

user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()

window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

red = (250, 0, 0)
blue = (0, 0, 250)
green = (0, 250, 0)
black = (0, 0, 0)
white = (250, 250, 250)

bg = pygame.image.load("rec/bg.jpg").convert_alpha()
bg2 = pygame.image.load("rec/bg2.jpg").convert_alpha()

spacesship = pygame.image.load("rec/spaceship.png").convert_alpha()
spacesship = pygame.transform.scale(spacesship, (50, 50))

spacesship2 = pygame.image.load("rec/spaceship2.png").convert_alpha()
spacesship2 = pygame.transform.scale(spacesship2, (50, 50))

explosionpic = pygame.image.load("rec/explosion.png").convert_alpha()
explosionpic = pygame.transform.scale(explosionpic, (50, 50))


bg = pygame.transform.scale(bg, (screen_width, screen_height))
