import utils


class Board:
    def __init__(self, scr, x: int, y: int, sx: int, sy: int, chs: dict, color = (0, 0)) -> None:
        self.scr = scr
        # self.x = x * 2 - 1
        self.x = x - sx
        self.y = y - sy // 2
        self.sx = sx * 2 - 1
        self.sy = sy
        self.chs = chs
        self.color = color

    def render(self):
        utils.drawRectFrame(self.scr, self.x - 1, self.y - 1, self.sx + 2, self.sy + 2, self.chs, self.color[0])
        utils.drawRect(self.scr, self.x, self.y, self.sx, self.sy, self.chs["inside"], self.color[1])
