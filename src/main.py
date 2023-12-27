"""Main module. Runs game"""


from game import Game


def main() -> None:
    """Runs game"""
    game = Game()
    game.main_loop()


if __name__ == '__main__':
    main()
