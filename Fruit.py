from random import randint, choice

import utils


class Fruit():
    def __init__(self, scr, x: int, y: int, possible_x: list[int], ch: str, color: int) -> None:
        self.scr = scr
        self.x = x
        self.possible_x = possible_x
        self.y = y
        self.ch = ch
        self.color = color

        self.score = 0

    def restart(self, board, body_coordinates: tuple) -> None:
        self.x = choice(self.possible_x)
        self.y = randint(board.y, board.y + board.sy - 1)
        while self.x in body_coordinates[0]:
            self.x = choice(self.possible_x)
        while self.y in body_coordinates[1]:
            self.y = randint(board.y, board.y + board.sy - 1)

    def render(self):
        utils.addstr(self.scr, self.x, self.y, self.ch, self.color)
