from settings import *
from classes import Block
from classes import Wall
from classes import Explosion
from classes import Player
from classes import Missile


def body(health):
    global bg2
    window.blit(bg2, (0, (screen_height - 300)))
    # pygame.draw.rect(window, black, (0, (screen_height - 200), screen_width, 200))
    pygame.draw.rect(window, red, (900, screen_height - 180, 300, 20))
    pygame.draw.rect(window, green, (900, screen_height - 180, health*3, 20))


def blub(times):
    for i in range(times):
        block = Block(None, spaceship, 50, 50, 1)

        block.rect.x = random.randint(-300, -50)
        block.rect.y = random.randint(75, screen_height - 450)

        block_list.add(block)
        all_sprites_list.add(block)


def blub2(times):
    for i in range(times):
        block2 = Block(None, spacesship2, 50, 50, 2)

        block2.rect.x = random.randint(-300, -50)
        block2.rect.y = random.randrange(75, screen_height - 450)

        block2_list.add(block2)
        all_sprites_list.add(block2)


def blub3(times):
    for i in range(times):
        bomber = Block(None, bomberpic, 200, 75, 4)

        bomber.rect.x = random.randint(-500, -200)
        bomber.rect.y = random.randrange(75, screen_height - 450)

        bomber_list.add(bomber)
        all_sprites_list.add(bomber)


def drop(x, y):
    zufall = random.randint(0, 4)
    if zufall == 1:
        drop_ammo = Block(None, ammo1, 25, 25, 0)
        drop_ammo.rect.x = x
        drop_ammo.rect.y = y

        ammo_drop_list.add(drop_ammo)
        all_sprites_list.add(drop_ammo)


class Endless:
    def __init__(self, health):
        super().__init__()
        self.keys = pygame.key.get_pressed()
        self.endless_run = True
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.count = 0
        self.mouse_visibility = pygame.mouse.set_visible(False)
        self.health = health
        self.score = 0
        self.ammo = ammo

    def run(self):
        # missile = Block(red, None, 5, 10, None)
        player = Player(spaceship, 50, 50)
        player.rect.x = screen_width/2
        cursor = Block(None, cursorpic, 40, 40, None)
        ammopic = Block(None, ammo1, 25, 25, 0)
        wall = Wall(red, 10, screen_height)
        wall_list.add(wall)
        cursor_list.add(cursor)
        ammopic_list.add(ammopic)
        all_sprites_list.add(wall)
        all_sprites_list.add(player)
        player_list.add(player)
        ammopic.rect.y = screen_height - 200
        ammopic.rect.x = 50
        blub(2)
        while self.endless_run:
            # clock
            clock.tick(120)
            # count for waves
            self.count += 1
            # drawing the layers
            window.blit(bg, (0, 0))
            body(self.health)
            self.mouse = pygame.mouse.get_pos()
            self.keys = pygame.key.get_pressed()
            # defining wall position
            wall.rect.x = screen_width - 100
            wall.rect.y = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.endless_run = False
                    if event.key == pygame.K_ESCAPE:
                        self.endless_run = False

                # shoot missiles
                if event.type == pygame.MOUSEBUTTONDOWN and self.ammo > 0:

                    if event.button == 1:
                        self.ammo -= 1
                        missile = Missile(white, 5, 10, self.mouse[0], self.mouse[1], player.rect.x, player.rect.y)
                        missile.rect.x = player.rect.x + 25
                        missile.rect.y = player.rect.y
                        missiles.add(missile)
                        all_sprites_list.add(missile)
                        missile.dest_x = self.mouse[0]
                        missile.dest_y = self.mouse[1]

            # moving the missile
            for missile in missiles:
                start_x = player.rect.x
                start_y = player.rect.y

                x_diff = missile.dest_x - start_x
                y_diff = missile.dest_y - start_y
                angle = math.atan2(y_diff, x_diff)
                # missile.angle = math.degrees(angle)
                change_x = math.cos(angle) * 20
                change_y = math.sin(angle) * 20

                missile.rect.x += change_x
                missile.rect.y += change_y

            # moving block
            for block in block_list:
                # speed
                block.rect.x += 1
            # moving block2
            for block2 in block2_list:
                # speed
                block2.rect.x += 3
            # moving bomber
            for bomber in bomber_list:
                # speed
                bomber.rect.x += 1

            # defining position of the cursor
            cursor.rect.x = self.mouse[0]
            cursor.rect.y = self.mouse[1]

            # defining position of the player
            player.rect.y = screen_height - 300
            if self.keys[pygame.K_a]:
                player.rect.x -= 10
            if self.keys[pygame.K_d]:
                player.rect.x += 10

            # Checking for all interactions of block
            for block in block_list:
                blocks_hit_list = pygame.sprite.spritecollide(block, missiles, True)
                end_screen = pygame.sprite.spritecollide(block, wall_list, False)
                bomber_exploded = pygame.sprite.spritecollide(block, bomber_exploded_list, False)

                if end_screen:
                    self.health -= 10
                    pygame.sprite.Sprite.kill(block)
                if blocks_hit_list:
                    block.health -= 1
                    print(block.health)
                if bomber_exploded:
                    self.score += 5
                    pygame.sprite.Sprite.kill(block)
                    explosion = Explosion(explosionpic, 50, 50)
                    explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
                    all_explosion.add(explosion)
                    all_sprites_list.add(explosion)
                if block.health <= 0:
                    self.score += 5
                    pygame.sprite.Sprite.kill(block)
                    explosion = Explosion(explosionpic, 50, 50)
                    explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
                    all_explosion.add(explosion)
                    all_sprites_list.add(explosion)
                    drop(block.rect.x, block.rect.y)

            # Checking for all interactions of block2
            for block in block2_list:
                blocks_hit_list = pygame.sprite.spritecollide(block, missiles, True)
                end_screen = pygame.sprite.spritecollide(block, wall_list, False)
                bomber_exploded = pygame.sprite.spritecollide(block, bomber_exploded_list, False)

                if end_screen:
                    self.health -= 20
                    pygame.sprite.Sprite.kill(block)
                if blocks_hit_list:
                    block.health -= 1
                    print(block.health)
                if bomber_exploded:
                    self.score += 5
                    pygame.sprite.Sprite.kill(block)
                    explosion = Explosion(explosionpic, 50, 50)
                    explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
                    all_explosion.add(explosion)
                    all_sprites_list.add(explosion)
                if block.health <= 0:
                    self.score += 5
                    pygame.sprite.Sprite.kill(block)
                    explosion = Explosion(explosionpic, 50, 50)
                    explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
                    all_explosion.add(explosion)
                    all_sprites_list.add(explosion)

            # checking for all interactions of bomber
            for bomber in bomber_list:
                blocks_hit_list = pygame.sprite.spritecollide(bomber, missiles, True)
                end_screen = pygame.sprite.spritecollide(bomber, wall_list, False)
                bomber_exploded = pygame.sprite.spritecollide(bomber, bomber_exploded_list, False)
                if end_screen:
                    self.health -= 20
                    pygame.sprite.Sprite.kill(bomber)
                if blocks_hit_list:
                    bomber.health -= 1
                    print(bomber.health)
                if bomber_exploded:
                    self.score += 15
                    pygame.sprite.Sprite.kill(bomber)
                    explosion = Explosion(bomber_explosion, 300, 150)
                    explosion.rect.x, explosion.rect.y = bomber.rect.x, bomber.rect.y
                    bomber_exploded_list.add(explosion)
                    all_sprites_list.add(explosion)
                if bomber.health <= 0:
                    self.score += 15
                    pygame.sprite.Sprite.kill(bomber)
                    explosion = Explosion(bomber_explosion, 300, 150)
                    explosion.rect.x, explosion.rect.y = bomber.rect.x, bomber.rect.y
                    bomber_exploded_list.add(explosion)
                    all_sprites_list.add(explosion)

            for player in player_list:
                player_pickup = pygame.sprite.spritecollide(player, ammo_drop_list, True)
                if player_pickup:
                    self.ammo += 10

            # Checking all interactions with ammo_drop
            for drop_ammo in ammo_drop_list:
                if drop_ammo.rect.y < screen_height - 300:
                    drop_ammo.rect.y += 2

            # Checking the countdown for explosions
            for explosion in all_explosion:
                explosion.explosion_count += 1
                if explosion.explosion_count >= 60:
                    pygame.sprite.Sprite.kill(explosion)
                    explosion.explosion_count = 0

            for explosion in bomber_exploded_list:
                explosion.explosion_count += 1
                if explosion.explosion_count >= 120:
                    pygame.sprite.Sprite.kill(explosion)
                    explosion.explosion_count = 0

            # Checking for all interaction of missile
            for missile in missiles:
                if missile.rect.y <= -10:
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
                if zufall == 2:
                    blub3(1)

            all_sprites_list.draw(window)
            cursor_list.draw(window)
            text = pygame.font.Font.render(font1, f"SCORE {self.score}", True, green)
            fps = pygame.font.Font.render(font2, str(int(clock.get_fps())), True, green)
            window.blit(text, (50, screen_height - 100))
            window.blit(fps, (10, 10))
            ammo_text = pygame.font.Font.render(font3, f"{self.ammo}", True, green)
            window.blit(ammo_text, (100, screen_height - 200))
            ammopic_list.draw(window)
            pygame.display.update()

        # after exiting, killing sprites
        for cursor in cursor_list:
            pygame.sprite.Sprite.kill(cursor)
        for player in all_sprites_list:
            pygame.sprite.Sprite.kill(player)
