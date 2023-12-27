"""Game and its mainloop"""


import pygame
from objects import Gun, Bullet, Enemy


class Game:
    """Game and its mainloop"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Space game')
        pygame.display.set_icon(pygame.image.load('images/icon.png'))

        # Player gun
        self.gun = Gun(self.screen, 1000, 700)
        self.gun_speed = 1

        # Bullets
        self.bullets = []

        # Enemies
        self.enemies = [
            Enemy(self.screen, 50, 150),
            Enemy(self.screen, 150, 250),
            Enemy(self.screen, 250, 350),
            Enemy(self.screen, 350, 450),
            Enemy(self.screen, 450, 550),
            Enemy(self.screen, 550, 660),
        ]

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

            for bullet in self.bullets:
                bullet.update()

            for enemy in self.enemies:
                enemy.draw()

                for bullet in self.bullets:
                    if bullet.image.colliderect(enemy.image_rect):
                        self.enemies.remove(enemy)
                        pygame.mixer.Sound('sounds/enemy_kill.mp3').play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.screen, self.gun)
                        self.bullets.append(bullet)
                        pygame.mixer.Sound('sounds/shooting.mp3').play()

            pygame.display.update()
