"""Enemy"""


import pygame


class Enemy:
    """Enemy"""
    def __init__(self, screen, x, y) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y

        self.__image = pygame.transform.scale(
            pygame.image.load('images/enemy.png'),
            (70, 70))
        self.__image_rect = self.__image.get_rect(
            topleft=(self.__x, self.__y))

    @property
    def image_rect(self):
        """Get image rect"""
        return self.__image_rect

    def draw(self) -> None:
        """Draw enemy"""
        self.__screen.blit(self.__image, (self.__x, self.__y))
