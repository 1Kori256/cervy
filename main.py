import os
import pygame
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


    def web_init(self):
        self.n = Network(self)
        self.player_id = int(self.n.get_player())
        self.game_instance = self.n.send("get")

    def update(self) -> None:

        self.game_instance = self.n.send("get")


        self.input.update()
        self.vrt_space.update()
        self.renderer.render()
        self.window.render_screen()

        if self.input.keyboard_variables["ready"]:
            self.n.send("ready")
            print("lets go")
        elif self.vrt_space.updated:
            self.game_instance = self.n.send(self.vrt_space.worms[self.player_id].to_string())
        else:
            self.n.send("check")


    def run(self) -> None:
        while True:
            self.update()


def menu_screen():
    app = App()

    run = True

    while run:
        app.window.clock.tick(60)
        app.window.window.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        app.window.window.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    app.web_init()
    app.run()


menu_screen()