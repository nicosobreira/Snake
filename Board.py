import utils


class Board:
    def __init__(self, scr, x: int, y: int, sx: int, sy: int, strings: dict, color = (0, 0)) -> None:
        self.scr = scr
        self.x = x - sx
        self.y = y - sy // 2
        self.sx = sx * 2 - 1
        self.sy = sy
        self.strings = strings
        self.color = color

        self.score = 0
        self.max_score = sx * sy


    def render(self):
        # Score
        utils.drawRectFrame(self.scr, self.x - 1, self.y - 3, self.sx + 2, 3, self.strings, self.color[0])
        message = f"{self.score}"
        utils.addstr(self.scr, self.sx // 2 + self.x - len(message) + 1, self.y - 2, message)
        
        # Board
        utils.drawRectFrame(self.scr, self.x - 1, self.y - 1, self.sx + 2, self.sy + 2, self.strings, self.color[0])
        utils.drawRect(self.scr, self.x, self.y, self.sx, self.sy, self.strings["inside"], self.color[1])
