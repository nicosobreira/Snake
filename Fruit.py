from random import randint, choice

import utils


# TODO the fruit spawn seams to be tilt to the sides
# TODO in certain parts the game crash and don't respond to the keyboard


class Fruit():
    def __init__(self, scr: None, possible_x: list[int],ch: str, color: int) -> None:
        self.scr = scr
        self.possible_x = possible_x
        self.ch = ch
        self.color = color

    def restart(self, board, body_coordinates) -> None:
        self.x = choice(self.possible_x)
        self.y = randint(board.y, board.y + board.sy - 1)
        while self.x in body_coordinates[0]:
            self.x = choice(self.possible_x)
        while self.y in body_coordinates[1]:
            self.y = randint(board.y, board.y + board.sy - 1)

    def render(self):
        utils.addstr(self.scr, self.x, self.y, self.ch, self.color)
