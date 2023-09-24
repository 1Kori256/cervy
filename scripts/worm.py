"""

"""


import pygame, random


def scale_image(img):
    return pygame.transform.scale(img, (32, 32))


class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y: return True
        return False

    def __sub__(self, other):
        return Block(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Block(self.x + other.x, self.y + other.y)

class Worm:
    def __init__(self, player_id, size, pos = None) -> None:
        self.player_id = player_id
        self.size = size
        if pos is None:
            self.body = [Block(9, 10), Block(8, 10), Block(7, 10)]
        else:
            self.body = [Block(*pos), Block(pos[0] - 1, pos[1]), Block(pos[0] - 2, pos[1])]
        self.direction = Block(1, 0)
        self.new_block = False

        self.head_up = scale_image(pygame.image.load('data/images/head_up.png').convert_alpha())
        self.head_down = scale_image(pygame.image.load('data/images/head_down.png').convert_alpha())
        self.head_right = scale_image(pygame.image.load('data/images/head_right.png').convert_alpha())
        self.head_left = scale_image(pygame.image.load('data/images/head_left.png').convert_alpha())
		
        self.tail_up = scale_image(pygame.image.load('data/images/tail_up.png').convert_alpha())
        self.tail_down = scale_image(pygame.image.load('data/images/tail_down.png').convert_alpha())
        self.tail_right = scale_image(pygame.image.load('data/images/tail_right.png').convert_alpha())
        self.tail_left = scale_image(pygame.image.load('data/images/tail_left.png').convert_alpha())

        self.body_vertical = scale_image(pygame.image.load('data/images/body_vertical.png').convert_alpha())
        self.body_horizontal = scale_image(pygame.image.load('data/images/body_horizontal.png').convert_alpha())

        self.body_tr = scale_image(pygame.image.load('data/images/body_tr.png').convert_alpha())
        self.body_tl = scale_image(pygame.image.load('data/images/body_tl.png').convert_alpha())
        self.body_br = scale_image(pygame.image.load('data/images/body_br.png').convert_alpha())
        self.body_bl = scale_image(pygame.image.load('data/images/body_bl.png').convert_alpha())

    def update(self, food, warm2) -> None:
        if food.pos == self.body[0]:
            self.new_block = True
            food.generate_pos()

        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def update_head_image(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Block(1,0): self.head = self.head_left
        elif head_relation == Block(-1,0): self.head = self.head_right
        elif head_relation == Block(0,1): self.head = self.head_up
        elif head_relation == Block(0,-1): self.head = self.head_down

    def update_tail_image(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Block(1,0): self.tail = self.tail_left
        elif tail_relation == Block(-1,0): self.tail = self.tail_right
        elif tail_relation == Block(0,1): self.tail = self.tail_up
        elif tail_relation == Block(0,-1): self.tail = self.tail_down

    def draw(self, surface) -> None:
        self.update_head_image()
        self.update_tail_image()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * self.size)
            y_pos = int(block.y * self.size)
            block_rect = pygame.Rect(x_pos, y_pos, self.size, self.size)

            if index == 0:
                surface.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                surface.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    surface.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    surface.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        surface.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        surface.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        surface.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        surface.blit(self.body_br, block_rect)
    
    def get_worm(self):
        return ";".join([f"{block.x}_{block.y}" for block in self.body])


    def set_worm(self, body_str):
        print(body_str)
        self.body = [Block(int(x), int(y)) for x, y in [block.split("_") for block in body_str.split(";")]]


class Food:
    def __init__(self, size) -> None:
        self.size = size
        self.generate_pos()
        self.image = scale_image(pygame.image.load('data/images/apple.png').convert_alpha())

    def draw(self, surface) -> None:
        fruit_rect = pygame.Rect(int(self.pos.x * self.size), int(self.pos.y * self.size), self.size, self.size)
        surface.blit(self.image, fruit_rect)

    def generate_pos(self) -> None:
        self.pos = Block(random.randint(0, 20), random.randint(0, 20))