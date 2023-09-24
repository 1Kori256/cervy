"""
Renderer object
"""

import pygame
import scripts.utilities as utilities


class Renderer:
    def __init__(self, app) -> None:
        
        """Initialize Renderer object.
        
        Keyword arguments:
        app - Main application class
        """
        
        self.app = app
        self.config = app.config
        
    def render(self) -> None:
        
        """Renders everything"""
        
        self.surface = self.app.window.app_window
        size = self.app.vrt_space.size 
        for i in range(30):
            for j in range(30):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(self.surface, (30, 30, 30), (i * size, j * size, size, size))


        self.app.vrt_space.food.draw(self.surface)
        for worm in self.app.vrt_space.worms[:self.app.game_instance.active_players]:
            worm.draw(self.surface)

        # Show debug values
        utilities.debug(self.surface, self.app.window.font, (750, 10), self.app.window.fps)