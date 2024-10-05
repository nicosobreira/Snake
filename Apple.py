from random import randint, choice

import utils


class Apple():
    def __init__(self, scr, x: int, y: int, possible_x: list[int], ch: str, color: int) -> None:
        self.scr = scr
        self.x = x
        self.possible_x = possible_x
        self.y = y
        self.ch = ch
        self.color = color

        self.score = 0

    def restart(self, board, player) -> None:
        while self.x == player.x:
            self.x = choice(self.possible_x)
        while self.y == player.y:
            self.y = randint(board.y, board.y + board.sy - 1)

    def render(self):
        utils.addstr(self.scr, self.x, self.y, self.ch, self.color)
