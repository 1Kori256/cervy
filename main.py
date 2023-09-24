import os
import scripts.utilities as utilities
from scripts.window import Window
from scripts.input import Input
from scripts.renderer import Renderer
from scripts.virtual_space import VrtSpace
from scripts.worm import Worm

from scripts.network import Network
clientNumber = 0


class App:
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = utilities.load_config(os.path.join(self.path, "config"))
            
        self.window = Window(self)
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.vrt_space = VrtSpace(self)

        self.n = Network(self)
        self.vrt_space.test_worm = Worm(1, self.vrt_space.size)
        self.vrt_space.test_worm2 = Worm(2, self.vrt_space.size)


    def update(self) -> None:

        p2_body_str = self.n.send(self.vrt_space.test_worm.get_worm())
        self.vrt_space.test_worm2.set_worm(p2_body_str)

        self.input.update()
        self.vrt_space.update()
        self.renderer.render()
        self.window.render_screen()


    def run(self) -> None:
        while True:
            self.update()


App().run()