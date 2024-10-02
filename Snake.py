import curses
import utils


class Snake:
    def __init__(self, scr, body: list[tuple], sx: int, sy: int, ch: str, color: int) -> None:
        self.scr = scr
        self.KEYS = {
            "up": 119,
            "down": 115,
            "left": 97,
            "right": 100,
        }
        self.body = body

        self.sx = sx
        self.sy = sy

        self.vx = 2
        self.vy = 2

        self.ch = ch
        self.color = color

    def input(self, key):
        if key == self.KEYS["up"]:
            self.vy = -self.vy
        elif key == self.KEYS["down"]:
            self.vy = abs(self.vy)
        elif key == self.KEYS["left"]:
            self.vx = -self.vx
        elif key == self.KEYS["right"]:
            self.vx = abs(self.vx)

    def update(self, max_size):
        x_head = self.body[0][0]
        y_head = self.body[0][1]
        self.body.append((x_head + self.vx, y_head + self.vy))
        if len(self.body) > max_size:
            del self.body[0]

    def render(self):
        for part in self.body:
            utils.drawRect(self.scr, part[0], part[1],
                           self.sx, self.sy, self.ch, self.color)
