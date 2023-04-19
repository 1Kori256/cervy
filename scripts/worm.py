"""

"""


import pygame, random


class Worm:
    def __init__(self, player_id) -> None:
        self.player_id = player_id
        self.head_pos = [10, 10]
        self.length = 3
        self.tail = [[7, 10], [8, 10], [9, 10]]
        self.dir = [1, 0]

    def update(self, food, warm2) -> None:
        self.tail.append(self.head_pos.copy())
        self.head_pos[0] += self.dir[0]
        self.head_pos[1] += self.dir[1]
        if food.pos == self.head_pos:
            food.generate_pos()
        else:
            self.tail.pop(0)

        is_dead = any([self.check_collision(self), self.check_collision(warm2)])
        print(is_dead)

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (255, 0, 0), (self.head_pos[0] * 20, self.head_pos[1] * 20, 20, 20))
        for tail_part_pos in self.tail:
            pygame.draw.rect(surface, (0, 255, 0), (tail_part_pos[0] * 20, tail_part_pos[1] * 20, 20, 20))

    def check_collision(self, other) -> bool:
        if self.player_id != other.player_id and self.head_pos == other.head_pos:
            return True
        for tail_part in other.tail:
            if self.head_pos == tail_part:
                return True
        
        return False

class Food:
    def __init__(self) -> None:
        self.generate_pos()

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (0, 0, 255), (self.pos[0] * 20, self.pos[1] * 20, 20, 20))

    def generate_pos(self) -> None:
        self.pos = [random.randint(0, 20), random.randint(0, 20)]