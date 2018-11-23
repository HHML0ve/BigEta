import pygame
from pygame.locals import *


class Brush(object):
    def __init__(self, screen):
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 1
        self.drawing = False
        self.last_pose = None

    def start_draw(self, pose):
        self.drawing = True
        self.last_pose = pose

    def end_draw(self):
        self.drawing = False

    def draw(self, pose):
        if self.drawing:
            pygame.draw.line(self.screen, self.color, self.last_pose, pose, self.size)
            self.last_pose = pose


class Painter(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Painter')
        self.clock = pygame.time.Clock()
        self.brush = Brush(self.screen)

    def run(self):
        self.screen.fill((255, 255, 255))
        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.screen.fill((255, 255, 255))
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.brush.start_draw((x, y))
                elif event.type == MOUSEMOTION:
                    self.brush.draw(event.pos)
                elif event.type == MOUSEBUTTONUP:
                    self.brush.end_draw()

            pygame.display.update()


if __name__ == '__main__':
    app = Painter()
    app.run()
