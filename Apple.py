from random import randint

import utils


class Apple():
    def __init__(self, scr: None, x: int, y: int, ch: str, color: int) -> None:
        self.scr = scr
        self.x = x
        self.y = y
        self.ch = ch
        self.color = color

        self.score = 0

    def restart(self, board):
        self.x = randint(board.x, board.x + board.sx - 1)
        self.y = randint(board.y, board.y + board.sy - 1)

    def render(self):
        utils.addstr(self.scr, self.x, self.y, self.ch, self.color)
