import random
import time
from .worm import Worm, Food

import pygame
pygame.init()
pygame.display.set_mode([960, 960])

start_worms = [
    Worm(0, 32, (10, 10)),
    Worm(1, 32, (10, 20)),
    Worm(2, 32, (20, 10)),
    Worm(3, 32, (20, 20)),
]

class GameInstance():
    def __init__(self, id):
        self.id = id
        self.active_players = 1
        self.food = Food(32)
        self.worms = []
        self.ready = False
        self.started = False

    def set_worms(self):
        for i in range(self.active_players):
            self.worms.append(start_worms[i])

    def is_ready(self):
        if self.ready:
            self.set_worms()
            time.sleep(3)
            self.started = True

    def update(self):
        if self.started:
            for i in range(self.active_players):
                self.worms[i].update(self.food)

    def reset():
        pass