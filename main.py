import os
import scripts.utilities as utilities
from scripts.window import Window
from scripts.input import Input
from scripts.renderer import Renderer
from scripts.virtual_space import VrtSpace
from scripts.worm import Worm

from scripts.network import Network


def parse_data(data):
    worms_data, update, player_id = data.split("&")
    worms_data = worms_data.split("|")
    if update == "True":
        update = True
    else:
        update = False
    return player_id, update, worms_data


class App:
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = utilities.load_config(os.path.join(self.path, "config"))
            
        self.window = Window(self)
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.vrt_space = VrtSpace(self)

        self.n = Network(self)
        start_worm = self.n.get_data()
        self.player_id, _, worm_data = parse_data(self.n.get_data())
        start_worm = worm_data[self.player_id]
        self.vrt_space.worm = Worm(self.player_id, self.vrt_space.size)
        self.vrt_space.worm.set_worm(start_worm)

        self.vrt_space.other_worms = [Worm(0, self.vrt_space.size), Worm(1, self.vrt_space.size), Worm(2, self.vrt_space.size), Worm(3, self.vrt_space.size)]


    def update(self) -> None:

        _, update, worm_data = parse_data(self.n.send(self.vrt_space.test_worm.get_worm()))

        for i in range(4):
            self.vrt_space.other_worms[i].set_worm(worm_data[i])

        if update:
            self.vrt_space.move_worms = True
        else:
            self.vrt_space.move_worms = False

        self.input.update()
        self.vrt_space.update()
        self.renderer.render()
        self.window.render_screen()


    def run(self) -> None:
        while True:
            self.update()


App().run()