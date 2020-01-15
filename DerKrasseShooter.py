from settings import *
from endless import Endless
from classes import Background
from classes import Block


def start_screen():
    # setting these vars into global
    global run, buttonpic, clock, health, mouse_visibility, fps

    # killing all sprites from the game-loop
    for block in block_list:
        pygame.sprite.Sprite.kill(block)
    for block in block2_list:
        pygame.sprite.Sprite.kill(block)
    for explosion in all_explosion:
        pygame.sprite.Sprite.kill(explosion)

    # init background
    sc1_background = Background(sc_bg3, 1)
    sc1_background2 = Background(sc_bg3, 1)
    background_list.add(sc1_background)
    background_list.add(sc1_background2)
    sc_background = Background(sc_bg2, 2)
    sc_background2 = Background(sc_bg2, 2)
    background_list.add(sc_background)
    background_list.add(sc_background2)
    background = Background(sc_bg1, 3)
    background2 = Background(sc_bg1, 3)
    background_list.add(background)
    background_list.add(background2)



    background.rect.x = 0
    background2.rect.x = screen_width
    sc_background.rect.x = 0
    sc_background2.rect.x = screen_width
    sc1_background.rect.x = 0
    sc1_background2.rect.x = screen_width

    # init mouse
    mouse_box = Block(red, None, 10, 10, 0)
    mouse_list.add(mouse_box)

    # here starts the loop
    start_screen_run = True
    mouse_visibility = pygame.mouse.set_visible(True)
    while start_screen_run:
        # the clock aka. max fps
        clock.tick(30)

        # setting the health value to default
        health = 100

        # getting information's from mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # defining the the mouse-hitbox
        mouse_box.rect.x = mouse[0]
        mouse_box.rect.y = mouse[1]

        # checking for events like quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen_run = False
                if event.key == pygame.K_x:
                    pygame.quit()

        # moving the background to side
        for background in background_list:
            if background.layer == 1:
                background.rect.x -= 1
            if background.layer == 2:
                background.rect.x -= 2
            if background.layer == 3:
                background.rect.x -= 3
            if background.rect.x <= -screen_width:
                pygame.sprite.Sprite.kill(background)
                background_list.add(background)
                background.rect.x = screen_width

        # drawing everything
        window.fill(black)
        background_list.draw(window)
        fps = pygame.font.Font.render(font2, str(int(clock.get_fps())), True, green)
        window.blit(fps, (10, 10))
        window.blit(title2, ((screen_width/2) - (titelx/2), (screen_height/2) - (titely/2)))
        button_list.draw(window)
        mouse_list.draw(window)
        pygame.display.flip()

    mouse_visibility = pygame.mouse.set_visible(False)
    for bg in background_list:
        pygame.sprite.Sprite.kill(bg)
    # after exiting killing all sprites
    for mouse in mouse_list:
        pygame.sprite.Sprite.kill(mouse)


mouse_visibility = pygame.mouse.set_visible(True)
run = True
while run:
    clock.tick(30)

    start_screen()
    endless = Endless(100)
    endless.run()

pygame.quit()
