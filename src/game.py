"""Game and its mainloop"""


import pygame


class Game:
    """Game and its mainloop"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Space game')
        pygame.display.set_icon(pygame.image.load('images/icon.png'))

    def main_loop(self):
        """Game mainloop"""
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

            pygame.display.update()
