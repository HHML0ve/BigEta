import pygame
from sys import exit

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('opposite movement')


class Sport(pygame.sprite.Sprite):

    def __init__(self, init_pose):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pose

        self.speed = 6

    def update(self, *args):
        self.rect.top += self.speed
        if self.rect.top >= SCREEN_HEIGHT:
            self.rect.top -= self.speed
            self.rect.left += self.speed
        elif self.rect.left >= SCREEN_WIDTH:
            self.rect.left -= self.speed
            self.rect.top += self.speed


sport = Sport([120, 120])
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))
    screen.blit(sport.image, sport.rect)
    sport.update()

    pygame.display.update()
