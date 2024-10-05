import curses
import utils

from Player import Player
from Apple import Apple

# TODO Fazer um método render no objeto Apple
# TODO O Player nake sai andando por ai, arrumar isso


class Board:
    def __init__(self, scr: None, x: int, y: int, sx: int, sy: int, chs: dict, color = 0) -> None:
        self.scr = scr
        self.x = x * 2 - 1
        self.y = y
        self.sx = sx * 2 - 1
        self.sy = sy
        self.chs = chs
        self.color = color

    def render(self):
        utils.drawRectFrame(self.scr, self.x - 1, self.y - 1, self.sx + 2, self.sy + 2, self.chs, 4)
        utils.drawRect(self.scr, self.x, self.y, self.sx, self.sy, "•", 5)
    

class Game:
    def __init__(self, stdscr):
        self.scr = stdscr
        self.scr.nodelay(True) # Se não tiver input o padrão é -1
        
        # Set color
        curses.start_color()
        curses.use_default_colors()

        curses.noecho() # Não exibe os inputs
        curses.curs_set(0) # Não mostra o cursor
       
        # Color pairs
        curses.init_pair(1, 2, -1) # Green 
        curses.init_pair(2, 3, -1) # Yellow
        curses.init_pair(3, 4, -1) # Blue
        curses.init_pair(4, 5, -1) # Roxo
        curses.init_pair(5, 8, -1) # Cinza
        
        self.state = True
        
        self.KEYS = {
            "q": 113,
            "r": 114
        }
        self.TICKRATE = 2
        

        self.score = 0
        self.board = Board(
            self.scr,
            4,
            5,
            10,
            10,
            {"horizontal": "-", "vertical": "|", "border": "+"},
            4
        )
        
        self.player = Player(
            self.scr,
            self.board.x + self.board.sx // 2,
            self.board.y + self.board.sy // 2,
            "o",
            1
        )

        self.apple = Apple(
            self.scr,
            (self.board.x + self.board.sx + 2) // 2,
            self.board.y + self.board.sy // 2,
            "*",
            2
        )

    def restart(self):
        self.player.restart(self.board)
        self.apple.restart(self.board)
        self.score = 0

    def Update(self):
        self.player.update(self.apple.score)
        
        if (    self.player.x <= self.board.x - 1 or
                self.player.x >= self.board.x + self.board.sx or
                self.player.y <= self.board.y - 1 or
                self.player.y >= self.board.y + self.board.sy):
            self.restart()

        if (    self.player.x == self.apple.x and
                self.player.y == self.apple.y):
            self.apple.restart(self.board)
            pass
        key = self.scr.getch()
        
        self.player.input(key)
        
        if key == self.KEYS["q"]:
            self.state = False

    
    def Render(self):
        self.scr.erase()
        
        self.board.render()
        self.player.render()
        self.apple.render()

        self.scr.refresh()


    def Loop(self):
        while self.state:
            self.Update()
            self.Render()

            curses.flushinp() # Faz com que os inputs não se "arrastem"
            curses.napms(1000 // self.TICKRATE)

def main(stdscr):
    game = Game(stdscr)
    game.Loop()

if __name__ == "__main__":
    curses.wrapper(main)
    # cupper(game.Loop)
