import curses
import utils


# TODO remake the get_coordinates_body, so it won't be necessary to reset the tuple


class Player():
    def __init__(self, scr: None, ch: str, color: int) -> None:
        self.scr = scr
        self.ch = ch
        self.color = color

        self.KEYS = {
            "up": (119, 107, curses.KEY_UP),
            "down": (115, 106, curses.KEY_DOWN),
            "left": (97, 104, curses.KEY_LEFT),
            "right": (100, 108, curses.KEY_RIGHT),
        }
        
        self.body = []
        self.body_coordinates = self.get_coordinates_body()
        self.vx = -2
        self.vy = 0

    def input(self, key: int) -> None:
        # For the input be successful the key must be pressed and you can't go backwards 
        if key in self.KEYS["up"] and self.vy != 1:
            self.vy = -1
            self.vx = 0
        elif key in self.KEYS["down"] and self.vy != -1:
            self.vy = 1
            self.vx = 0
        elif key in self.KEYS["left"] and self.vx != 2:
            self.vx = -2
            self.vy = 0
        elif key in self.KEYS["right"] and self.vx != -2:
            self.vx = 2
            self.vy = 0

    def get_coordinates_body(self) -> None:
        self.body_coordinates = ([], [])
        for coordinate in self.body:
            self.body_coordinates[0].append(coordinate[0])
            self.body_coordinates[1].append(coordinate[1])
    
    def restart(self, board) -> None:
        self.x = board.x + board.sx // 2
        if board.sx % 2 != 0:
            self.x += 1
        self.y = board.y + board.sy // 2
        self.body = [(self.x, self.y)]
    
    def render(self) -> None:
        ###
        for part in self.body:
            utils.addstr(self.scr, part[0], part[1], self.ch, self.color)
