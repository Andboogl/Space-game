"""Module to work with player score"""


import os


class Score:
    """Class to work with player score"""
    def __init__(self) -> None:
        self.__score = 0
        self.__best_score_file = 'best_score.txt'

        try:
            with open(self.__best_score_file, encoding='utf-8') as best_score_file:
                self.__best_score = int(best_score_file.read())

        except Exception:
            self.__best_score = None

    def load_score(self) -> None:
        """Load score to score file"""
        if not self.__best_score:
            to_write = True

        else:
            if self.__best_score < self.__score:
                to_write = True

            else:
                to_write = False

        if to_write:
            format_ = 'a' if not os.path.exists(self.__best_score_file) else 'w'

            with open(self.__best_score_file, format_, encoding='utf-8') as file:
                file.write(str(self.__score))

            self.__best_score = int(self.__score)

    def update(self):
        """Update score data"""
        self.__init__()

    def add_score(self, score=10) -> None:
        """Add score to score"""
        self.__score += score

    @property
    def score(self) -> int:
        """Get best score"""
        return self.__score

    @property
    def best_score(self) -> int:
        """Get best score"""
        return self.__best_score
