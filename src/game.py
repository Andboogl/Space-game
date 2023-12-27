"""Game and its mainloop"""


import pygame
from objects import Gun, Bullet, Enemy
from score import Score
from game_over import GameOverScreen
from spawn import generate_enemies_coordinates


class Game:
    """Game and its mainloop"""
    def __init__(self) -> None:
        pygame.init()

        self.__screen = pygame.display.set_mode((1200, 800))
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption('Space game')
        pygame.display.set_icon(pygame.image.load('images/icon.png'))

        self.__points_font = pygame.font.Font('fonts/RubikScribble.ttf', 50)

        self.init()

    def init(self) -> None:
        """Init game"""
        # Player gun
        self.__gun = Gun(self.__screen, 1000, 700)
        self.__gun_speed = 7

        # Playing atributes
        self.__play_mode = 'Playing'

        # Bullets
        self.__bullets = []

        # Enemies
        enemies_coordinates = generate_enemies_coordinates(6)

        self.__enemies = [
            Enemy(self.__screen,
                  enemies_coordinates[0][0], enemies_coordinates[0][1]),
            Enemy(self.__screen,
                enemies_coordinates[1][0], enemies_coordinates[1][1]),
            Enemy(self.__screen,
                enemies_coordinates[2][0], enemies_coordinates[2][1]),
            Enemy(self.__screen,
                enemies_coordinates[3][0], enemies_coordinates[3][1]),
            Enemy(self.__screen,
                enemies_coordinates[4][0], enemies_coordinates[4][1]),
            Enemy(self.__screen,
                enemies_coordinates[5][0], enemies_coordinates[5][1])
        ]

        # Score
        self.__score = Score()

    def __draw_enemies(self):
        """Draw enemies"""
        # Drawing enemies
        for enemy in self.__enemies:
            enemy.draw()

            # Bullet enemy kill
            try:
                for bullet in self.__bullets:
                    if bullet.image.colliderect(enemy.image_rect):
                        self.__enemies.remove(enemy)
                        self.__bullets.remove(bullet)
                        self.__score.add_score()

                        enemy_coordinate = generate_enemies_coordinates(1)
                        self.__enemies.append(Enemy(self.__screen,
                            enemy_coordinate[0][0], enemy_coordinate[0][1]))
                        pygame.mixer.Sound('sounds/enemy_kill.mp3').play()

            # If two bullets hit the enemy at once.
            except Exception:
                pass

            # Player kill
            if self.__gun.image_rect.colliderect(enemy.image_rect):
                self.__play_mode = 'Game over'
                pygame.mixer.Sound('sounds/loss.mp3').play()

            # Lose when the enemy is at the bottom of the map
            if enemy.image_rect.y >= 800 - enemy.image_rect.height:
                self.__play_mode = 'Game over'
                pygame.mixer.Sound('sounds/loss.mp3').play()

            enemy.update()

    def __draw_bullets(self):
        """Draw bullets"""
        for bullet in self.__bullets:
            bullet.update()

            if bullet.image.y <= 0 - bullet.image.height:
                self.__bullets.remove(bullet)

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

                self.__draw_bullets()
                self.__draw_enemies()

                self.__score.load_score()

                # Drawing score text
                score_text = self.__points_font.render(str(self.__score.score), True, (255, 255, 255))
                self.__screen.blit(score_text, (1200 / 2 - score_text.get_width(), 10))

            elif self.__play_mode == 'Game over':
                game_over_screen = GameOverScreen(self.__screen, self.__score)
                self.__play_mode = game_over_screen.draw()

                if self.__play_mode == 'Playing':
                    self.init()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                elif event.type == pygame.KEYDOWN and self.__play_mode == 'Playing':
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.__screen, self.__gun)
                        self.__bullets.append(bullet)
                        pygame.mixer.Sound('sounds/shooting.mp3').play()

            pygame.display.update()
            self.__clock.tick(60)
