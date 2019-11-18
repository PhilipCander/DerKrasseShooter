import pygame
import random
import ctypes

user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()

#screen_width, screen_height = 1366, 768

window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

red = (250, 0, 0)
green = (0, 250, 250)
black = (0, 0, 0)
white = (250, 250, 250)

bg = pygame.image.load("rec/bg.jpg")
