from settings import *
from scummbag import Block
block_list = pygame.sprite.Group()
block2_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()
speed = 90
wave = 3
wave2 = 1


def blub():
    global wave
    global block
    global block_list
    global all_sprites_list
    for i in range(wave):
        block = Block(green, 50, 50)

        block.rect.x = random.randint(-300, -50)
        block.rect.y = random.randrange(screen_height-50)

        block_list.add(block)
        all_sprites_list.add(block)


def blub2():
    global wave2
    global block2
    global block2_list
    global all_sprites_list
    for i in range(wave2):
        block2 = Block(red, 50, 50)

        block2.rect.x = random.randint(-200, -50)
        block2.rect.y = random.randrange(screen_height-50)

        block2_list.add(block2)
        all_sprites_list.add(block2)


player = Block(red, 3, 3)
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

    window.fill(black)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for block in block_list:
        block.rect.x += 3

    for block2 in block2_list:
        block2.rect.x += 5

    player.rect.x = mouse[0]
    player.rect.y = mouse[1]

    if click[0] == 1:
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        blocks2_hit_list = pygame.sprite.spritecollide(player, block2_list, True)

        print(block_list)

    if count >= speed:
        blub()
        zufall = random.randint(0, 4)
        if zufall == 1:
            blub2()
        count = 0

    all_sprites_list.draw(window)
    pygame.display.update()

pygame.quit()
