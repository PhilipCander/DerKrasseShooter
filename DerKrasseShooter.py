from settings import *
from endless import Endless
from classes import Background


def start_screen():
    global run
    global clock
    global health
    global mouse_visibility
    background = Background(bg)
    background2 = Background(bg)
    background_list.add(background)
    background_list.add(background2)

    background.rect.x = 0
    background2.rect.x = screen_width



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
                    pygame.quit()
        for block in block_list:
            pygame.sprite.Sprite.kill(block)
        for block in block2_list:
            pygame.sprite.Sprite.kill(block)
        for explosion in all_explosion:
            pygame.sprite.Sprite.kill(explosion)

        for background in background_list:
            background.rect.x -= 1
            if background.rect.x <= -screen_width:
                pygame.sprite.Sprite.kill(background)
                background_list.add(background)
                background.rect.x = screen_width
        window.fill(black)
        background_list.draw(window)
        window.blit(title2, ((screen_width/2) - (titelx/2), (screen_height/2) - (titely/2)))

        pygame.display.flip()
    mouse_visibility = pygame.mouse.set_visible(False)


mouse_visibility = pygame.mouse.set_visible(True)
run = True
while run:
    clock.tick(30)

    start_screen()
    endless = Endless(100)
    endless.run()

pygame.quit()
