import utils


class Apple:
    def __init__(self, scr, x: int, y: int, sx: int, sy: int, ch: str, color: int) -> None:
        self.scr = scr

        self.x = x
        self.y = y

        self.sx = sx
        self.sy = sy

        self.ch = ch
        self.color = color

        self.score = 0
