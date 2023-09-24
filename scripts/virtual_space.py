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

    
    def update(self) -> None:
        
        """Update in-game stuff"""

        if self.app.input.keyboard_variables["move_up"]:
            self.worm.direction = Block(0, -1)

        if self.app.input.keyboard_variables["move_down"]:
            self.worm.direction = Block(0, 1)

        if self.app.input.keyboard_variables["move_right"]:
            self.worm.direction = Block(1, 0)

        if self.app.input.keyboard_variables["move_left"]:
            self.worm.direction = Block(-1, 0)

        self.move_worms = False