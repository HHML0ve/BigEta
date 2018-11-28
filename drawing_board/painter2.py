# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import math


class Brush(object):
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 1
        self.drawing = False
        self.last_pose = None
        self.space = 1
        self.style = False
        self.brush = pygame.image.load('resource/brush.png').convert_alpha()
        self.brush_now = self.brush.subsurface((0, 0), (1, 1))

    def start_draw(self, pose):
        self.drawing = True
        self.last_pose = pose

    def end_draw(self):
        self.drawing = False

    def set_brush_style(self, style):
        self.style = style

    def get_brush_style(self):
        return self.style

    def get_current_brush(self):
        return self.brush_now

    def set_size(self, size):
        if size < 0.5:
            size = 0.5
        elif size > 32:
            size = 32
        self.size = size
        self.brush_now = self.brush.subsurface((0, 0), (size * 2, size * 2))

    def get_size(self):
        return self.size

    def set_color(self, b_color):
        self.color = b_color
        # 循环是为了把图片 resource/brush.png 填充满
        for i in range(self.brush.get_width()):
            for j in range(self.brush.get_height()):
                # b_color 是一个tuple， 只能和tuple相加
                # 单元素tuple 加一个逗号是为了防止和声明一个整形歧义
                # a 是颜色的alpha
                self.brush.set_at((i, j), b_color)
                # self.brush.set_at((i, j), b_color + (self.brush.get_at((i, j)).a,))

    def get_color(self):
        return self.color

    def draw(self, pose):
        if self.drawing:
            for p in self._get_points(pose):
                if not self.style:
                    pygame.draw.circle(self.screen, self.color, p, int(self.size))
                else:
                    self.screen.blit(self.brush_now, p)

            self.last_pose = pose

    def _get_points(self, pose):
        """ Get all points between last_point ~ now_point. """
        points = [(self.last_pose[0], self.last_pose[1])]
        len_x = pose[0] - self.last_pose[0]
        len_y = pose[1] - self.last_pose[1]
        length = math.sqrt(len_x ** 2 + len_y ** 2)
        step_x = len_x / length
        step_y = len_y / length
        for i in range(int(length)):
            points.append(
                (points[-1][0] + step_x, points[-1][1] + step_y))
        points = map(lambda x: (int(0.5 + x[0]), int(0.5 + x[1])), points)
        return list(set(points))


class Menu(object):
    def __init__(self, screen):
        self.screen = screen
        self.brush = None
        self.colors = [
            (0xff, 0x00, 0xff), (0x80, 0x00, 0x80),
            (0x00, 0x00, 0xff), (0x00, 0x00, 0x80),
            (0x00, 0xff, 0xff), (0x00, 0x80, 0x80),
            (0x00, 0xff, 0x00), (0x00, 0x80, 0x00),
            (0xff, 0xff, 0x00), (0x80, 0x80, 0x00),
            (0xff, 0x00, 0x00), (0x80, 0x00, 0x00),
            (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff),
            (0x00, 0x00, 0x00), (0x80, 0x80, 0x80),
        ]
        self.colors_rect = []
        for (i, rgb) in enumerate(self.colors):
            # 一个 Rect 对象可以由 left，top，width，height 几个值创建
            rect = pygame.Rect(10 + i % 2 * 32, 254 + i / 2 * 32, 32, 32)
            self.colors_rect.append(rect)

        self.pens = [
            pygame.image.load("resource/pen1.png").convert_alpha(),
            pygame.image.load("resource/pen2.png").convert_alpha()
        ]

        self.pens_rect = []
        for (i, img) in enumerate(self.pens):
            rect = pygame.Rect(10, 10 + i * 64, 64, 64)
            self.pens_rect.append(rect)

        self.sizes = [
            pygame.image.load("resource/big.png").convert_alpha(),
            pygame.image.load("resource/small.png").convert_alpha()
        ]
        self.sizes_rect = []
        for (i, img) in enumerate(self.sizes):
            rect = pygame.Rect(10 + i * 32, 138, 32, 32)
            self.sizes_rect.append(rect)

    def set_brush(self, brush):
        self.brush = brush

    def draw(self):
        # draw pen style button
        for (i, img) in enumerate(self.pens):
            self.screen.blit(img, self.pens_rect[i].topleft)
        # draw < > buttons
        for (i, img) in enumerate(self.sizes):
            self.screen.blit(img, self.sizes_rect[i].topleft)
        # draw current pen / color
        self.screen.fill((255, 255, 255), (10, 180, 64, 64))
        pygame.draw.rect(self.screen, (0, 0, 0), (10, 180, 64, 64), 1)
        size = self.brush.get_size()
        x = 10 + 32
        y = 180 + 32
        if self.brush.get_brush_style():
            x = x - size
            y = y - size
            self.screen.blit(self.brush.get_current_brush(), (x, y))
        else:
            pygame.draw.circle(self.screen,
                               self.brush.get_color(), (x, y), int(size))
        # draw colors panel
        for (i, rgb) in enumerate(self.colors):
            pygame.draw.rect(self.screen, rgb, self.colors_rect[i])

    def click_button(self, pos):
        # pen buttons
        for (i, rect) in enumerate(self.pens_rect):
            if rect.collidepoint(pos):
                self.brush.set_brush_style(bool(i))
                return True
        # size buttons
        for (i, rect) in enumerate(self.sizes_rect):
            if rect.collidepoint(pos):
                if i:  # i == 1, size down
                    self.brush.set_size(self.brush.get_size() - 0.5)
                else:
                    self.brush.set_size(self.brush.get_size() + 0.5)
                return True
        # color buttons
        for (i, rect) in enumerate(self.colors_rect):
            if rect.collidepoint(pos):
                self.brush.set_color(self.colors[i])
                return True
        return False


class Painter(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Painter')
        self.clock = pygame.time.Clock()
        self.brush = Brush(self.screen)
        self.menu = Menu(self.screen)
        self.menu.set_brush(self.brush)

    def run(self):
        self.screen.fill((255, 255, 255))
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.screen.fill((255, 255, 255))
                elif event.type == MOUSEBUTTONDOWN:
                    # self.brush.start_draw(event.pos)
                    # <= 74, coarse judge here can save much time
                    if ((event.pos)[0] <= 74 and self.menu.click_button(event.pos)):
                        # if not click on a functional button, do drawing
                        # 此处是点到了工具栏
                        pass
                    else:
                        self.brush.start_draw(event.pos)
                elif event.type == MOUSEMOTION:
                    self.brush.draw(event.pos)
                elif event.type == MOUSEBUTTONUP:
                    self.brush.end_draw()
            # 这就是为什么没有显示状态栏的原因
            self.menu.draw()
            pygame.display.update()


if __name__ == '__main__':
    app = Painter()
    app.run()
