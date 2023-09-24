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
        
        self.app.vrt_space.food.draw(self.surface)
        self.app.vrt_space.worm.draw(self.surface)
        for i, worm in enumerate(self.app.vrt_space.other_worms):
            if i != self.app.player_id:
                worm.draw(self.surface)

        # Show debug values
        utilities.debug(self.surface, self.app.window.font, (750, 10), self.app.window.fps)