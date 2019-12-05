from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, color, pic, width, height, health):
        super().__init__()
        self.color = color
        self.pic = pic
        self.health = health
        self.width = width
        self.height = height
        self.pos = None
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


class Player(pygame.sprite.Sprite):
    def __init__(self, pic, width, height):
        super().__init__()
        self.pic = pic
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha(self.image)
        self.image.blit(self.pic, (0, 0))

        self.rect = self.image.get_rect()


class Missile(pygame.sprite.Sprite):
    def __init__(self, color, width, height, mouse_x, mouse_y, start_x, start_y):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image = self.image.convert_alpha(self.image)
        self.dest_x = 0
        self.dest_y = 0
        pygame.draw.ellipse(self.image, color, [0, 0, width, height], 0)

        # does not work yet
        self.start_x = start_x
        self.start_y = start_y
        self.dest_x = mouse_x
        self.dest_y = mouse_y
        self.diff_x = self.dest_x - self.start_x
        self.diff_y = self.dest_y - self.start_y

        print("test", self.diff_x, self.diff_y)
        self.angle = math.atan2(self.diff_y, self.diff_x)
        self.angle = math.degrees(self.angle)

        self.change_x = math.cos(self.angle) * 10
        self.change_y = math.sin(self.angle) * 10
        self.rect = self.image.get_rect()
