"""Bullet"""


import pygame
from .gun import Gun


class Bullet:
    """Bullet"""
    def __init__(self, screen, gun: Gun):
        self.__gun = gun
        self.__screen = screen
        self.__x = self.__gun.x + 35
        self.__y = self.__gun.y - 30
        self.__color = 5, 255, 5 # Bullet color (RGB)
        self.__speed = 1
        self.__image = pygame.draw.line(
            self.__screen, self.__color,
            (self.__x, self.__y), (self.__x, self.__y + 50), 2)

    @property
    def image(self):
        """Get bullet image"""
        return self.__image

    def update(self):
        """Update bullet coordinates"""
        self.__y -= self.__speed
        self.__image = pygame.draw.line(self.__screen,
                                        self.__color,
                                        (self.__x, self.__y),
                                        (self.__x, self.__y + 50), 2)

    def draw_bullet(self):
        """Draw bullet"""
        self.__screen.blit(self.__image, (self.__x, self.__y))
