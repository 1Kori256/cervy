"""
Virtual space object
"""


from scripts.worm import Worm
import time


class VrtSpace:
    def __init__(self, app) -> None:
        
        """Initialize Virtual space object.
        
        Keyword arguments:
        app - Main application class
        """
        
        self.app = app
        self.config = app.config
        
        self.to_render = []

        self.move_worms = False
        self.start_time = time.time()

        self.test_worm = Worm()

        self.size = 20
    
    def update(self) -> None:
        
        """Update in-game stuff"""

        if time.time() - self.start_time >= 0.250:
            self.start_time = time.time()
            self.move_worms = True

        if self.app.input.keyboard_variables["move_up"]:
            self.test_worm.dir = [0, -1]

        if self.app.input.keyboard_variables["move_down"]:
            self.test_worm.dir = [0, 1]

        if self.app.input.keyboard_variables["move_right"]:
            self.test_worm.dir = [1, 0]

        if self.app.input.keyboard_variables["move_left"]:
            self.test_worm.dir = [-1, 0]

        if self.move_worms:
            self.test_worm.update()

        self.move_worms = False