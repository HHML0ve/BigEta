from random import randint

from game_role import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('beautiful snow')

player = Player([200, 600])

# 食物组
foods = pygame.sprite.Group()

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(10)
    # print(len(group.sprites()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    screen.blit(player.image, player.rect)

    foods.add(Food((randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))))
    foods.update()
    foods.draw(screen)

    pygame.display.update()

    # 操纵玩家移动
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
        player.move_up()
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
        player.move_down()
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
        player.move_left()
    if key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
        player.move_right()
