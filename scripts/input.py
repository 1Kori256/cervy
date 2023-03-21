"""
Handle user input
"""

import pygame, sys
from pygame.locals import *
import json

class Input:
    def __init__(self, app) -> None:
        
        """Initialize Input object.
        
        Keyword arguments:
        app - Main application class
        """
        
        self.app = app
        self.config = app.config
        self.implement = "main_game" # Only inputs allowed in here
        
        # Create dictionary for all buttons
        self.keyboard_variables, self.mouse_variables = {}, {}
        for bind, bind_data in self.config["input"].items():
            if bind_data["device"] == "keyboard":
                self.keyboard_variables[bind] = False
            elif bind_data["device"] == "mouse":
                self.mouse_variables[bind] = False
        
        self.reset_scroll("scroll_up", "scroll_down")
        
        self.mouse_pos = [0, 0]
        self.previous_mouse_pos = [0, 0]
        
    def reset_scroll(self, *scroll_bind) -> None:
        
        """Reset scroll buttons
        
        Keyword arguments:
        *scroll_bind: all scrolls that are to be reseted
        """
        
        for scroll in scroll_bind:
            self.mouse_variables[scroll] = {"test": False}
       
    def update(self) -> None:
        
        """Update user input"""
        
        # Transform mouse position
        mouse_pos = pygame.mouse.get_pos()
        self.previous_mouse_pos = self.mouse_pos
        self.mouse_pos = (int(mouse_pos[0] * (self.app.window.base_resolution[0] / self.app.window.scaled_resolution[0])),
                          int(mouse_pos[1] * (self.app.window.base_resolution[0] / self.app.window.scaled_resolution[0])))

        
        # Reset inputs that are triggered by press not by holding + scrolls
        self.reset_scroll("scroll_up", "scroll_down")
        for bind, bind_data in self.config["input"].items():
            if bind_data["device"] == "keyboard":
                if bind_data["trigger"] == "press":
                    self.keyboard_variables[bind] = False
            elif bind_data["device"] == "mouse":
                if bind_data["trigger"] == "press":
                    self.mouse_variables[bind] = False
                    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            # Update input dictionaries
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                keys_to_disable = []

                for bind, data in self.config["input"].items():
                    if self.implement in data["implement"]:
                        if data["device"] == "keyboard":
                            if keys[data["binding"]] == 1:
                                if data["trigger"] == "hold":
                                    self.keyboard_variables[str(bind)] = True
                                elif data["trigger"] == "press":
                                    self.keyboard_variables[str(bind)] = True
                                    keys_to_disable.append(str(bind))
                                elif data["trigger"] == "toggle":
                                    if event.type == pygame.KEYDOWN:
                                        if self.keyboard_variables[str(bind)]:
                                            self.keyboard_variables[str(bind)] = False
                                        else:
                                            self.keyboard_variables[str(bind)] = True
                            else:
                                if data["trigger"] == "hold":
                                    self.keyboard_variables[str(bind)] = False
                                
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                button = event.button
                button_status = (event.type == pygame.MOUSEBUTTONDOWN)

                for bind, data in self.config["input"].items():
                    if self.implement in data["implement"]:
                        if data["device"] == "mouse":
                            if data["button"] == button:
                                if button not in [4, 5]:
                                    self.mouse_variables[str(bind)] = button_status
                                else:
                                    pass

        # Quit application
        if self.keyboard_variables["exit"]:
            pygame.quit()
            sys.exit()
        