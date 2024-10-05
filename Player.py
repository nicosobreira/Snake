import curses
import utils


class Player():
    def __init__(self, scr: None, x: int, y: int, ch: str, color: int) -> None:
        self.scr = scr
        self.x = x
        self.y = y
        self.ch = ch
        self.color = color

        self.KEYS = {
            "up": (119, curses.KEY_UP),
            "down": (115, curses.KEY_DOWN),
            "left": (97, curses.KEY_LEFT),
            "right": (100, curses.KEY_RIGHT),
        }
        
        self.body = {}
        self.vx = -2
        self.vy = 0

    def input(self, key: int):
        if key in self.KEYS["up"]:
            self.vy = -1
            self.vx = 0
        elif key in self.KEYS["down"]:
            self.vy = 1
            self.vx = 0
        elif key in self.KEYS["left"]:
            self.vx = -2
            self.vy = 0
        elif key in self.KEYS["right"]:
            self.vx = 2
            self.vy = 0

    def restart(self, board):
        self.x = board.x + board.sx  // 2
        if board.sx % 2 == 0:
            self.x += 1
        self.y = board.y + board.sy // 2
    
    def update(self, max_size):
        self.x += self.vx
        self.y += self.vy

    def render(self):
        utils.addstr(self.scr, self.x, self.y, self.ch, self.color)
        # for part in self.body:
        #     utils.addstr(self.scr, part[0], part[1], self.ch["body"], self.color)
