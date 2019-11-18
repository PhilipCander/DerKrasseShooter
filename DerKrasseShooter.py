from settings import *
from classes import Block

block_list = pygame.sprite.Group()
block2_list = pygame.sprite.Group()
missles = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

speed = 90
wave = 3
wave2 = 1
cooldown = 100
shoot = False


def header():
    pygame.draw.rect(window, black, (0, 0, screen_width, 75))
    pygame.draw.rect(window, green, (((screen_width/2)-300), 50, 300, 20))


def body():
    pygame.draw.rect(window, black, (0, (screen_height-200), screen_width, 200))


def blub():
    global wave
    global block
    global block_list
    global all_sprites_list
    for i in range(wave):
        block = Block(green, 50, 50)

        block.rect.x = random.randint(-300, -50)
        block.rect.y = random.randint(75, screen_height-250)

        block_list.add(block)
        all_sprites_list.add(block)


def blub2():
    global wave2
    global block2
    global block2_list
    global all_sprites_list
    for i in range(wave2):
        block2 = Block(red, 50, 50)

        block2.rect.x = random.randint(-300, -50)
        block2.rect.y = random.randrange(75, screen_height-250)

        block2_list.add(block2)
        all_sprites_list.add(block2)

missle = Block(white, 5, 10)
player = Block(red, 25, 25)
all_sprites_list.add(player)

clock = pygame.time.Clock()

count = 0
blub()
run = True
while run:
    clock.tick(60)
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False

    window.blit(bg, (0, 0))
    #window.fill(white)
    header()
    body()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for missle in missles:
        missle.rect.y -= 10

    for block in block_list:
        block.rect.x += 3

    for block2 in block2_list:
        block2.rect.x += 5

    player.rect.x = mouse[0]
    player.rect.y = 600

    if click[0] == 1:
        missle = Block(white, 5, 10)
        missle.rect.x = mouse[0]
        missle.rect.y = 600
        missles.add(missle)
        all_sprites_list.add(missle)

    click = pygame.mouse.get_pressed()


    blocks_hit_list = pygame.sprite.spritecollide(missle, block_list, True)
    blocks2_hit_list = pygame.sprite.spritecollide(missle, block2_list, True)
    if blocks_hit_list:
        print("yeah")

    if count >= speed:
        blub()
        zufall = random.randint(0, 4)
        if zufall == 1:
            blub2()
        count = 0

    all_sprites_list.draw(window)
    pygame.display.update()

pygame.quit()
