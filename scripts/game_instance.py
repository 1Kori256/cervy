import random
import time
from .worm import Worm, Food

import pygame
pygame.init()
pygame.display.set_mode([960, 960])

start_worms = [
    Worm(0, 32, (5, 5)).to_array(),
    Worm(1, 32, (5, 25)).to_array(),
    Worm(2, 32, (25, 5)).to_array(),
    Worm(3, 32, (25, 25)).to_array(),
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
        self.update_worms = []
        self.set_worms()

    def set_worms(self):
        for i in range(self.active_players):
            self.worms.append(self.start_worms[i])
            self.update_worms.append(False)

    def is_ready(self):
        if self.ready:
            self.started = True

    def update(self):
        if self.started:
            for i in range(self.active_players):
                self.update_worms[i] = True

    def reset():
        pass