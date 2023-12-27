"""Gun"""


import pygame


class Gun:
    """Gun"""
    def __init__(self, screen, x: int, y: int, width=70, height=70) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y

        # Gun image
        self.__image = pygame.transform.scale(
            pygame.image.load('images/gun.png'),
            (width, height))

        self.__image_rect = self.__image.get_rect()
        self.__screen_rect = self.__screen.get_rect()

    @property
    def x(self):
        """Get gun x position"""
        return self.__x

    @property
    def y(self):
        """Get gun y position"""
        return self.__y

    def plus_x_position(self, pos):
        """
        Add number to x position
        Moving to right
        """
        if self.__x + self.__image_rect.width < self.__screen_rect.width:
            self.__x += pos

    def minus_x_position(self, pos):
        """
        Minus number from x position
        Moving to left
        """
        if self.__x > 0:
            self.__x -= pos

    def plus_y_position(self, pos):
        """
        Add number to y position
        Moving to down
        """
        if self.__y + self.__image_rect.height < self.__screen_rect.height:
            self.__y += pos

    def minus_y_position(self, pos):
        """
        Minus number from y position
        Moving to up
        """
        if self.__y > 0:
            self.__y -= pos

    def draw(self) -> None:
        """Draw gun"""
        self.__screen.blit(self.__image, (self.__x, self.__y))
