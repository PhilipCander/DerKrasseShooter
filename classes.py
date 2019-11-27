from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, color, pic, width, height, health):
        super().__init__()
        self.color = color
        self.pic = pic
        self.health = health
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha(self.image)
        if self.color is None:
            self.image.blit(self.pic, (0, 0))
        else:
            pygame.draw.ellipse(self.image, color, [0, 0, width, height], 0)

        self.rect = self.image.get_rect()


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        pygame.draw.rect(self.image, color, (0, 0, width, height))

        self.rect = self.image.get_rect()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pic, width, height):
        super().__init__()
        self.pic = pic
        self.width = width
        self.height = height
        self.explosion_count = 0
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha(self.image)
        self.image.blit(self.pic, (0, 0))

        self.rect = self.image.get_rect()


class Background(pygame.sprite.Sprite):
    def __init__(self, pic):
        super().__init__()
        self.pic = pic
        self.width = screen_width
        self.height = screen_height
        self.explosion_count = 0
        self.image = pygame.Surface([screen_width, screen_height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha(self.image)
        self.image.blit(self.pic, (0, 0))

        self.rect = self.image.get_rect()
