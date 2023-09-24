import random
import time
from .worm import Worm, Food

import pygame
pygame.init()
pygame.display.set_mode([960, 960])

start_worms = [
    Worm(0, 32, (10, 10)).to_array(),
    Worm(1, 32, (10, 20)).to_array(),
    Worm(2, 32, (20, 10)).to_array(),
    Worm(3, 32, (20, 20)).to_array(),
]

class GameInstance():
    def __init__(self, id):
        self.id = id
        self.active_players = 1
        self.food = (5, 5)
        self.worms = []
        self.ready = False
        self.started = False
        self.start_worms = start_worms

    def set_worms(self):
        for i in range(self.active_players):
            self.worms.append(self.start_worms[i])

    def is_ready(self):
        if self.ready:
            self.set_worms()
            time.sleep(3)
            self.started = True

    def update(self):
        if self.started:
            for i in range(self.active_players):
                pass

    def reset():
        pass