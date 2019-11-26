from settings import *
from classes import Block
from classes import Wall
from classes import Explosion


def header(health):
    pygame.draw.rect(window, black, (0, 0, screen_width, 75))
    pygame.draw.rect(window, red, (((screen_width / 2) - 300), 50, 300, 20))
    pygame.draw.rect(window, green, (((screen_width / 2) - 300), 50, (health*3), 20))


def body():
    global bg2
    bg2 = pygame.transform.scale(bg2, (screen_width, 200))
    window.blit(bg2, (0, (screen_height - 200)))
    # pygame.draw.rect(window, black, (0, (screen_height - 200), screen_width, 200))


def blub(times):
    for i in range(times):
        block = Block(None, spaceship, 50, 50, 1)

        block.rect.x = random.randint(-300, -50)
        block.rect.y = random.randint(75, screen_height - 250)

        block_list.add(block)
        all_sprites_list.add(block)


def blub2(times):
    for i in range(times):
        block2 = Block(None, spacesship2, 50, 50, 2)

        block2.rect.x = random.randint(-300, -50)
        block2.rect.y = random.randrange(75, screen_height - 250)

        block2_list.add(block2)
        all_sprites_list.add(block2)


class Endless:
    def __init__(self, health):
        super().__init__()
        self.endless_run = True
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.count = 0
        self.mouse_visibility = pygame.mouse.set_visible(False)
        self.health = health

    def run(self):
        # missile = Block(red, None, 5, 10, None)
        player = Block(red, None, 25, 25, None)
        wall = Wall(red, 10, screen_height)
        wall_list.add(wall)
        all_sprites_list.add(wall)
        all_sprites_list.add(player)
        blub(2)
        while self.endless_run:
            # clock
            clock.tick(120)
            # count for waves
            self.count += 1
            # drawing the layers
            window.blit(bg, (0, 0))
            header(self.health)
            body()
            self.mouse = pygame.mouse.get_pos()
            # defining wall position
            wall.rect.x = screen_width - 100
            wall.rect.y = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.endless_run = False
                    if event.key == pygame.K_ESCAPE:
                        self.endless_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        missile = Block(white, None, 5, 10, None)
                        missile.rect.x = self.mouse[0]
                        missile.rect.y = player.rect.y
                        missiles.add(missile)
                        all_sprites_list.add(missile)

            # moving the missile
            for missile in missiles:
                # speed
                missile.rect.y -= 20
            # moving block
            for block in block_list:
                # speed
                block.rect.x += 1
            # moving block2
            for block2 in block2_list:
                # speed
                block2.rect.x += 3
            # defining position of the player
            player.rect.x = self.mouse[0]
            player.rect.y = screen_height - 200

            # Checking for all interactions of block
            for block in block_list:
                blocks_hit_list = pygame.sprite.spritecollide(block, missiles, True)
                end_screen = pygame.sprite.spritecollide(block, wall_list, False)
                if end_screen:
                    self.health -= 10
                    pygame.sprite.Sprite.kill(block)
                if blocks_hit_list:
                    block.health -= 1
                    print(block.health)
                if block.health <= 0:
                    pygame.sprite.Sprite.kill(block)
                    explosion = Explosion(explosionpic, 50, 50)
                    explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
                    all_explosion.add(explosion)
                    all_sprites_list.add(explosion)

            # Checking for all interactions of block2
            for block in block2_list:
                blocks_hit_list = pygame.sprite.spritecollide(block, missiles, True)
                end_screen = pygame.sprite.spritecollide(block, wall_list, False)
                if end_screen:
                    self.health -= 20
                    pygame.sprite.Sprite.kill(block)
                if blocks_hit_list:
                    block.health -= 1
                    print(block.health)
                if block.health <= 0:
                    pygame.sprite.Sprite.kill(block)
                    explosion = Explosion(explosionpic, 50, 50)
                    explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
                    all_explosion.add(explosion)
                    all_sprites_list.add(explosion)

            # Checking for all interaction of block
            for explosion in all_explosion:
                explosion.explosion_count += 1
                if explosion.explosion_count >= 60:
                    pygame.sprite.Sprite.kill(explosion)
                    explosion.explosion_count = 0

            # Checking for all interaction of missile
            for missile in missiles:
                if missile.rect.y <= 75:
                    pygame.sprite.Sprite.kill(missile)

            # Checking for all interaction of health
            if self.health <= 1:
                self.endless_run = False

            # Checking for count to create new wave
            if self.count >= speed:
                blub(2)
                zufall = random.randint(0, 4)
                if zufall == 1:
                    blub2(1)
                self.count = 0

            all_sprites_list.draw(window)
            pygame.display.update()
        for player in all_sprites_list:
            pygame.sprite.Sprite.kill(player)
