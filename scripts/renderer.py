"""
Renderer object
"""

import pygame, random, math
from collections import OrderedDict
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
        
        # Show debug values
        utilities.debug(self.surface, self.app.window.font, (250, 10), self.app.window.fps)