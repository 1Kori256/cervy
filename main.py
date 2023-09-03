import os
import scripts.utilities as utilities
from scripts.window import Window
from scripts.input import Input
from scripts.renderer import Renderer
from scripts.virtual_space import VrtSpace
from scripts.worm import Worm

from scripts.network import Network
clientNumber = 1

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


class App:
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = utilities.load_config(os.path.join(self.path, "config"))
            
        self.window = Window(self)
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.vrt_space = VrtSpace(self)

        self.n = Network(self)
        start_pos = read_pos(self.n.getPos())
        self.vrt_space.test_worm = Worm(1, self.vrt_space.size, start_pos)
        self.vrt_space.test_worm2 = Worm(2, self.vrt_space.size, (10, 20))


    def update(self) -> None:

        p2_pos = read_pos(self.n.send(make_pos((self.vrt_space.test_worm.body[0].x, self.vrt_space.test_worm.body[0].y))))

        self.input.update()
        self.vrt_space.update()
        self.renderer.render()
        self.window.render_screen()


    def run(self) -> None:
        while True:
            self.update()


App().run()