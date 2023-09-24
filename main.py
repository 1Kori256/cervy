import os
import scripts.utilities as utilities
from scripts.window import Window
from scripts.input import Input
from scripts.renderer import Renderer
from scripts.virtual_space import VrtSpace
from scripts.worm import Worm

from scripts.network import Network


class App:
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.config = utilities.load_config(os.path.join(self.path, "config"))
            
        self.window = Window(self)
        self.input = Input(self)
        self.renderer = Renderer(self)
        self.vrt_space = VrtSpace(self)

        self.n = Network(self)
        self.player_id = self.n.get_player()
        self.game_instance = self.n.send("get")


    def update(self) -> None:

        self.game_instance = self.n.send("get")

        self.input.update()
        self.vrt_space.update()
        self.renderer.render()
        self.window.render_screen()

        self.game_instance = self.n.send()


    def run(self) -> None:
        while True:
            self.update()


App().run()