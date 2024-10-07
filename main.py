import curses

from Board import Board
from Player import Player
from Fruit import Fruit


class Game:
    def __init__(self, stdstdscr):
        self.stdscr = stdstdscr
        self.stdscr.nodelay(True) # Se não tiver input o padrão é -1
        
        # Set color
        curses.start_color()
        curses.use_default_colors()

        curses.noecho() # Não exibe os inputs
        curses.curs_set(0) # Não mostra o cursor
       
        # Color pairs
        curses.init_pair(1, 2, -1) # Green 
        curses.init_pair(2, 3, -1) # Yellow
        curses.init_pair(4, 5, -1) # Roxo
        curses.init_pair(5, 8, -1) # Cinza
        
        self.state = True
        
        self.KEYS = {
            "q": 113,
            "r": 114
        }
        self.TICKRATE = 2
 

        self.board = Board(
            self.stdscr,
            curses.COLS // 2,
            curses.LINES // 2,
            6,
            6,
            {"horizontal": "-", "vertical": "|", "border": "+", "inside": "•"},
            (4, 5)
        )

        self.player = Player(
            self.stdscr,
            "o",
            1
        )
        self.player.restart(self.board)
        self.player.get_coordinates_body()
        
        # Get only the x values that fit in the 2:1 ratio
        possible_x = [i for i in range(self.board.x, self.board.sx + self.board.x, 2)]
        
        self.fruit = Fruit(
            self.stdscr,
            possible_x,
            "*",
            2
        )
        self.fruit.restart(self.board, self.player.body_coordinates)

    def gameover(self):
        self.player.restart(self.board)
        self.fruit.restart(self.board, self.player.body_coordinates)
        self.board.score = 0

    def Update(self):
        self.player.x += self.player.vx
        self.player.y += self.player.vy

        # Collision: Player x Board
        if (    self.player.x <= self.board.x - 1 or # Left
                self.player.x >= self.board.x + self.board.sx or # Right
                self.player.y <= self.board.y - 1 or # Up
                self.player.y >= self.board.y + self.board.sy): # Down
            self.gameover()
        
        # Collision: Player head x Player body
        ###
        for part in self.player.body:
            if (    self.player.x == part[0] and
                    self.player.y == part[1]):
                self.gameover()
        
        self.player.get_coordinates_body()
        
        # Insert new head
        self.player.body.insert(0, (self.player.x, self.player.y))
        
        # Collision: Player head x Fruit
        ###
        if (    self.player.x == self.fruit.x and
                self.player.y == self.fruit.y):
            self.fruit.restart(self.board, self.player.body_coordinates)
            self.board.score += 1
        else:
            self.player.body.pop()

        if self.board.score == self.board.max_score:
            self.state = False

        # Input
        key = self.stdscr.getch()
        
        self.player.input(key)
        
        if key == self.KEYS["q"]:
            self.state = False

    
    def Render(self):
        self.stdscr.erase()
        
        self.board.render()
        self.player.render()
        self.fruit.render()

        self.stdscr.refresh()


    def Loop(self):
        while self.state:
            self.Update()
            self.Render()

            curses.flushinp() # Faz com que os inputs não se "arrastem"
            curses.napms(1000 // self.TICKRATE)

def main(stdstdscr):
    game = Game(stdstdscr)
    game.Loop()

if __name__ == "__main__":
    curses.wrapper(main)
