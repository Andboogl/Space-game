"""Game and its mainloop"""


import pygame
from objects import Gun, Bullet, Enemy
from score import Score


class Game:
    """Game and its mainloop"""
    def __init__(self) -> None:
        pygame.init()

        self.__screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Space game')
        pygame.display.set_icon(pygame.image.load('images/icon.png'))

        self.init()

    def init(self) -> None:
        """Init game"""
        # Player gun
        self.__gun = Gun(self.__screen, 1000, 700)
        self.__gun_speed = 1

        # Playing atributes
        self.__play_mode = 'Playing'

        # Bullets
        self.__bullets = []

        # Enemies
        self.__enemies = [
            Enemy(self.__screen, 50, 150),
            Enemy(self.__screen, 150, 250),
            Enemy(self.__screen, 250, 350),
            Enemy(self.__screen, 350, 450),
            Enemy(self.__screen, 450, 550),
            Enemy(self.__screen, 550, 660),
        ]

        # Score
        self.__score = Score()

    def main_loop(self) -> None:
        """Game mainloop"""
        while True:
            if self.__play_mode == 'Playing':
                self.__screen.fill((0, 0, 0))
                self.__gun.draw()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_a]:
                    self.__gun.minus_x_position(self.__gun_speed)

                if keys[pygame.K_s]:
                    self.__gun.plus_y_position(self.__gun_speed)

                if keys[pygame.K_d]:
                    self.__gun.plus_x_position(self.__gun_speed)

                if keys[pygame.K_w]:
                    self.__gun.minus_y_position(self.__gun_speed)

                # Drawing bullets
                for bullet in self.__bullets:
                    bullet.update()

                # Drawing enemies
                for enemy in self.__enemies:
                    enemy.draw()

                    # Bullet enemy kill
                    for bullet in self.__bullets:
                        if bullet.image.colliderect(enemy.image_rect):
                            self.__enemies.remove(enemy)
                            self.__score.add_score()
                            pygame.mixer.Sound('sounds/enemy_kill.mp3').play()

                    # Player kill
                    if self.__gun.image_rect.colliderect(enemy.image_rect):
                        self.__play_mode = 'Game over'
                        self.__score.load_score()

            elif self.__play_mode == 'Game over':
                self.init()
                self.__play_mode = 'Playing'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                elif event.type == pygame.KEYDOWN and self.__play_mode == 'Playing':
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.__screen, self.__gun)
                        self.__bullets.append(bullet)
                        pygame.mixer.Sound('sounds/shooting.mp3').play()

            pygame.display.update()
