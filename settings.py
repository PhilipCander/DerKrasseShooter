import pygame
import random
import ctypes
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

# defining vars for the game
speed = 90
wave = 1
wave2 = 1
shoots = 1
run = False
health = 100
clock = pygame.time.Clock()

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

# setting resolution
if screen_height == 1080 and screen_width == 1920:
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

    spacesship2 = pygame.image.load("rec/spaceship2.png").convert_alpha()
    spacesship2 = pygame.transform.scale(spacesship2, (50, 50))

    explosionpic = pygame.image.load("rec/explosion.png").convert_alpha()
    explosionpic = pygame.transform.scale(explosionpic, (50, 50))
    bomber_explosion = pygame.image.load("rec/explosion.png").convert_alpha()
    bomber_explosion = pygame.transform.scale(bomber_explosion, (300, 150))
