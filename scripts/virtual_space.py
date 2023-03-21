"""
Virtual space object
"""


class VrtSpace:
    def __init__(self, app) -> None:
        
        """Initialize Virtual space object.
        
        Keyword arguments:
        app - Main application class
        """
        
        self.app = app
        self.config = app.config
        
        self.to_render = []
    
    def update(self) -> None:
        
        """Update in-game stuff"""

        pass