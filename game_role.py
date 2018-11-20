# -*- coding: utf-8 -*-
import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


class Player(pygame.sprite.Sprite):
    def __init__(self, init_pose):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pose

        self.speed = 30
        self.is_hit = False
        self.weight = 0

    # 控制玩家长大
    def grow_up(self, food):
        if food:
            self.image = pygame.Surface(self.rect.width + 0.1, self.rect.height + 0.1)
            self.weight = (self.rect.width + 0.1) * (self.rect.height + 0.1)
            if self.speed % 2 == 0:
                self.speed -= 1

    def move_up(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        self.rect.top -= self.speed

    def move_down(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        self.rect.top += self.speed

    def move_left(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        self.rect.left -= self.speed

    def move_right(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        self.rect.left += self.speed


class Food(pygame.sprite.Sprite):
    def __init__(self, init_pose):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pose
