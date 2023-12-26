"""Game and its mainloop"""


import pygame
from objects import Gun


class Game:
    """Game and its mainloop"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Space game')
        pygame.display.set_icon(pygame.image.load('images/icon.png'))

        # Player gun
        self.gun = Gun(self.screen, 500, 500)
        self.gun_speed = 1

    def main_loop(self):
        """Game mainloop"""
        while True:
            self.screen.fill((0, 0, 0))
            self.gun.draw()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.gun.minus_x_position(self.gun_speed)

            if keys[pygame.K_s]:
                self.gun.plus_y_position(self.gun_speed)

            if keys[pygame.K_d]:
                self.gun.plus_x_position(self.gun_speed)

            if keys[pygame.K_w]:
                self.gun.minus_y_position(self.gun_speed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

            pygame.display.update()
