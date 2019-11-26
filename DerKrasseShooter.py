from settings import *
from classes import Block
from classes import Wall
from endless import Endless


def start_screen():
    global run
    global clock
    global health
    global mouse_visibility
    start_screen_run = True
    mouse_visibility = pygame.mouse.set_visible(True)
    while start_screen_run:
        clock.tick(30)
        health = 100
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen_run = False
                if event.key == pygame.K_x:
                    return run
        for block in block_list:
            pygame.sprite.Sprite.kill(block)
        for block in block2_list:
            pygame.sprite.Sprite.kill(block)
        for explosion in all_explosion:
            pygame.sprite.Sprite.kill(explosion)

        window.fill(red)
        pygame.display.update()
    mouse_visibility = pygame.mouse.set_visible(False)


mouse_visibility = pygame.mouse.set_visible(True)
run = True
while run:
    clock.tick(30)
    start_screen()
    endless = Endless(100)
    endless.run()


pygame.quit()
