import os
import scripts.utilities as utilities
from scripts.window import Window
from scripts.input import Input
from scripts.renderer import Renderer
from scripts.virtual_space import VrtSpace

class App:
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = utilities.load_config(os.path.join(self.path, "config"))
            
        self.window = Window(self)
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.vrt_space = VrtSpace(self)


    def update(self) -> None:
        self.input.update()
        self.vrt_space.update()
        self.renderer.render()
        self.window.render_screen()

    
    def run(self) -> None:
        while True:
            self.update()


App().run()