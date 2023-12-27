"""Game over screen"""


import pygame
from score import Score


class GameOverScreen:
    """Game over screen"""
    def __init__(self, main_screen, score: Score) -> None:
        self.__screen = main_screen
        self.__screen_rect = self.__screen.get_rect()

        self.__score = score
        self.__title_font = pygame.font.Font('fonts/RubikScribble.ttf', 128)
        self.__option_font = pygame.font.Font('fonts/RubikScribble.ttf', 64)
        self.__text_color = (255, 255, 255)

    def draw(self) -> str:
        """Draw game over screen"""
        self.__screen.fill((0, 0, 0))

        # Title text
        self.__screen.blit(
            self.__title_font.render('Game over!', True, self.__text_color),
            (233, 24))

        # Score
        score_text = self.__option_font.render(
            f'Score: {self.__score.score}',
            True, self.__text_color)
        self.__screen.blit(score_text, (
            self.__screen_rect.width / 2 - score_text.get_width() / 2, 200))

        # Best score
        best_score_text = self.__option_font.render(
            f'Best score: {self.__score.best_score}',
            True, self.__text_color)
        self.__screen.blit(best_score_text, (
            self.__screen_rect.width / 2 - best_score_text.get_width() / 2, 297))

        return 'Game over' # Returns play mode
