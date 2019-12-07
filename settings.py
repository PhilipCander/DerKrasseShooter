import pygame
import random
import ctypes
import math
math.acos(1)
randomInit = random.randint(0, 0)

# getting screensize for formatting the window
user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()

# defining the window
window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# defining some colors
red = (250, 0, 0)
blue = (0, 0, 250)
green = (0, 250, 0)
black = (0, 0, 0)
white = (250, 250, 250)
font1 = pygame.font.Font("rec/FFFFORWA.TTF", 30)
font2 = pygame.font.Font("rec/FFFFORWA.TTF", 10)


# defining vars for the game
speed = 90
wave = 1
wave2 = 1
run = False
health = 100
clock = pygame.time.Clock()
fps = pygame.font.Font.render(font1, str(int(clock.get_fps())), True, blue)

# creating sprite-groups
block_list = pygame.sprite.Group()
block2_list = pygame.sprite.Group()
bomber_list = pygame.sprite.Group()
missiles = pygame.sprite.Group()
all_explosion = pygame.sprite.Group()
bomber_exploded_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
background_list = pygame.sprite.Group()
cursor_list = pygame.sprite.Group()
button_list = pygame.sprite.Group()

buttonpic = pygame.image.load("rec/button1.png").convert_alpha()

cursorpic = pygame.image.load("rec/cursor.png").convert_alpha()
cursorpic = pygame.transform.scale(cursorpic, (40, 40))

title1 = pygame.image.load("rec/Titel1.png").convert_alpha()
title2 = pygame.image.load("rec/Titel2.png").convert_alpha()
titelx = 930
titely = 264



bg = pygame.image.load("rec/bg.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (screen_width, screen_height))
bg2 = pygame.image.load("rec/bg2.jpg").convert_alpha()
bg2 = pygame.transform.scale(bg2, (screen_width, (screen_height - 500)))
spaceship = pygame.image.load("rec/spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship, (50, 50))

bomberpic = pygame.image.load("rec/bomber.png").convert_alpha()
bomberpic = pygame.transform.scale(bomberpic, (200, 75))

spacesship2 = pygame.image.load("rec/spaceship2.png").convert_alpha()
spacesship2 = pygame.transform.scale(spacesship2, (50, 50))

explosionpic = pygame.image.load("rec/explosion.png").convert_alpha()
explosionpic = pygame.transform.scale(explosionpic, (50, 50))
bomber_explosion = pygame.image.load("rec/explosion.png").convert_alpha()
bomber_explosion = pygame.transform.scale(bomber_explosion, (300, 150))
