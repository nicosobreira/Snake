from utils import addstr

class Entity:
    def __init__(self, scr: None, x: int, y: int, ch: str, color=0) -> None:
        self.scr = scr
        self.x = x
        self.y = y
        
        if (self.x - 7) % 2 != 0:
            self.x += 1

        self.ch = ch
        self.color = color

    def render(self):
