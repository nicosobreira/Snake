import curses
import utils


class Player:
    def __init__(self, scr, body: list[tuple], sx: int, sy: int, ch: str, color: int) -> None:
        self.scr = scr
        self.KEYS = {
            "up": (119, curses.KEY_UP),
            "down": (115, curses.KEY_DOWN),
            "left": (97, curses.KEY_LEFT),
            "right": (100, curses.KEY_RIGHT),
        }
        self.body = body

        self.sx = sx
        self.sy = sy

        self.vx = -self.sx
        self.vy = 0

        self.ch = ch
        self.color = color

    def input(self, key):
        if key in self.KEYS["up"]:
            self.vy = -self.sy
            self.vx = 0
        elif key in self.KEYS["down"]:
            self.vy = self.sy
            self.vx = 0
        elif key in self.KEYS["left"]:
            self.vx = -self.sx
            self.vy = 0
        elif key in self.KEYS["right"]:
            self.vx = self.sx
            self.vy = 0

    def update(self, max_size):
        x_head = self.body[0][0]
        y_head = self.body[0][1]
        self.body.append((x_head + self.vx, y_head + self.vy))
        if len(self.body) > max_size:
            self.body.pop(0)

    def render(self):
        for part in self.body:
            utils.drawRect(self.scr, part[0], part[1], self.sx, self.sy, self.ch, self.color)
