from random import randint

from game_role import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Eta Eta Eta ... ')

player = Player([200, 600])

# 食物组
foods = pygame.sprite.Group()

clock = pygame.time.Clock()
running = True
full_screen = False

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

    foods_eta_list = pygame.sprite.spritecollide(player, foods, True)
    if len(foods_eta_list) > 0:
        player.grow_up(True)

    # 绘制得分
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(player.weight), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)

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

    if key_pressed[pygame.K_f]:
        full_screen = not full_screen
        if full_screen:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE)
        else:
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 48)
text = font.render('Score: %s' % player.weight, True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
