"""

"""


import pygame


class Worm:
    def __init__(self):
        self.pos = [10, 10]
        self.dir = [1, 0]

    def update(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.pos[0] * 20, self.pos[1] * 20, 20, 20))