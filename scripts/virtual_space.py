"""
Virtual space object
"""


from scripts.worm import Worm, Food, Block
import time


class VrtSpace:
    def __init__(self, app) -> None:
        
        """Initialize Virtual space object.
        
        Keyword arguments:
        app - Main application class
        """
        
        self.app = app
        self.config = app.config
                
        self.size = 32

        self.move_worms = False
        self.start_time = time.time()

        self.food = Food(self.size)
        self.updated = False

        self.worms = [0, 1, 2, 3]
        for i in range(4):
            self.worms[i] = Worm(i, self.size)

    
    def update(self) -> None:
        
        """Update in-game stuff"""


        for i in range(self.app.game_instance.active_players):
            self.worms[i].body = [Block(*block) for block in self.app.game_instance.worms[i]]

        if self.app.input.keyboard_variables["move_up"]:
            self.worms[self.app.player_id].direction = Block(0, -1)

        if self.app.input.keyboard_variables["move_down"]:
            self.worms[self.app.player_id].direction = Block(0, 1)

        if self.app.input.keyboard_variables["move_right"]:
            self.worms[self.app.player_id].direction = Block(1, 0)

        if self.app.input.keyboard_variables["move_left"]:
            self.worms[self.app.player_id].direction = Block(-1, 0)

        self.updated = False
        if self.app.game_instance.update_worms[self.app.player_id]:
            self.worms[self.app.player_id].update(self.food)
            self.updated = True

        self.move_worms = False