from settings import *
from classes import Block
from classes import Wall

block_list = pygame.sprite.Group()
block2_list = pygame.sprite.Group()
missles = pygame.sprite.Group()
all_explosion = pygame.sprite.Group()
walllist = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


speed = 90
wave = 1
wave2 = 1
cooldown = 100
shoots = 1
explosioncount = 0
run = False
health = 100
clock = pygame.time.Clock()
count = 0


def header():
    global health
    pygame.draw.rect(window, black, (0, 0, screen_width, 75))
    pygame.draw.rect(window, red, (((screen_width / 2) - 300), 50, 300, 20))
    pygame.draw.rect(window, green, (((screen_width / 2) - 300), 50, (health*3), 20))


def body():
    global bg2
    bg2 = pygame.transform.scale(bg2, (screen_width, 200))
    window.blit(bg2, (0, (screen_height - 200)))
    # pygame.draw.rect(window, black, (0, (screen_height - 200), screen_width, 200))



def startscreen():
    global run
    global clock
    global health
    global ingame
    startscreenrun = True
    ingame = pygame.mouse.set_visible(True)
    while startscreenrun:
        clock.tick(30)
        health = 100
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    startscreenrun = False
        for block in block_list:
            pygame.sprite.Sprite.kill(block)
        for block in block2_list:
            pygame.sprite.Sprite.kill(block)
        for explosion in all_explosion:
            pygame.sprite.Sprite.kill(explosion)

        window.fill(red)
        pygame.display.update()
    ingame = pygame.mouse.set_visible(False)


def blub():
    global wave
    global block
    global block_list
    global all_sprites_list
    for i in range(wave):
        block = Block(None, spacesship, 50, 50, 1)

        block.rect.x = random.randint(-300, -50)
        block.rect.y = random.randint(75, screen_height - 250)

        block_list.add(block)
        all_sprites_list.add(block)


def blub2():
    global wave2
    global block2
    global block2_list
    global all_sprites_list
    for i in range(wave2):
        block2 = Block(None, spacesship2, 50, 50, 2)

        block2.rect.x = random.randint(-300, -50)
        block2.rect.y = random.randrange(75, screen_height - 250)

        block2_list.add(block2)
        all_sprites_list.add(block2)


missle = Block(red, None, 5, 10, None)
player = Block(red, None, 25, 25, None)
wall = Wall(red, 10, screen_height)
walllist.add(wall)
all_sprites_list.add(wall)
all_sprites_list.add(player)


startscreen()
blub()
ingame = pygame.mouse.set_visible(False)
while run:
    clock.tick(120)
    count += 1
    window.blit(bg, (0, 0))
    header()
    body()

    wall.rect.x = screen_width - 100
    wall.rect.y = 0

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                missle = Block(white, None, 5, 10, None)
                missle.rect.x = mouse[0]
                missle.rect.y = 600
                missles.add(missle)
                all_sprites_list.add(missle)

    for missle in missles:
        missle.rect.y -= 20

    for block in block_list:
        block.rect.x += 3

    for block2 in block2_list:
        block2.rect.x += 5

    player.rect.x = mouse[0]
    player.rect.y = 600

# Checking for all interactions of block
    for block in block_list:
        blocks_hit_list = pygame.sprite.spritecollide(block, missles, True)
        endscreen = pygame.sprite.spritecollide(block, walllist, False)
        if endscreen:
            health -= 10
            pygame.sprite.Sprite.kill(block)
        if blocks_hit_list:
            block.health -= 1
            print(block.health)
        if block.health <= 0:
            pygame.sprite.Sprite.kill(block)
            explosion = Block(None, explosionpic, 50, 50, None)
            explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
            all_explosion.add(explosion)
            all_sprites_list.add(explosion)

# Checking for all interactions of block2
    for block in block2_list:
        blocks_hit_list = pygame.sprite.spritecollide(block, missles, True)
        endscreen = pygame.sprite.spritecollide(block, walllist, False)
        if endscreen:
            health -= 20
            pygame.sprite.Sprite.kill(block)
        if blocks_hit_list:
            block.health -= 1
            print(block.health)
        if block.health <= 0:
            pygame.sprite.Sprite.kill(block)
            explosion = Block(None, explosionpic, 50, 50, None)
            explosion.rect.x, explosion.rect.y = block.rect.x, block.rect.y
            all_explosion.add(explosion)
            all_sprites_list.add(explosion)

    for explosion in all_explosion:
        explosioncount += 1
        if explosioncount >= 60:
            pygame.sprite.Sprite.kill(explosion)
            explosioncount = 0

    for missle in missles:
        if missle.rect.y <= 75:
            pygame.sprite.Sprite.kill(missle)

    if health <= 1:
        startscreen()

    if count >= speed:
        blub()
        zufall = random.randint(0, 4)
        if zufall == 1:
            blub2()
        count = 0

    all_sprites_list.draw(window)
    pygame.display.update()

pygame.quit()
