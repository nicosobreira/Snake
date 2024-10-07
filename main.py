import curses

from Board import Board
from Player import Player
from fruit import Fruit


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
        curses.init_pair(4, 5, -1) # Roxo
        curses.init_pair(5, 8, -1) # Cinza
        
        self.state = True
        
        self.KEYS = {
            "q": 113,
            "r": 114
        }
        self.TICKRATE = 4
 

        self.board = Board(
            self.scr,
            curses.COLS // 2,
            curses.LINES // 2,
            5,
            5,
            {"horizontal": "-", "vertical": "|", "border": "+", "inside": "•"},
            (4, 5)
        )

        self.player = Player(
            self.scr,
            self.board.x + self.board.sx // 2,
            self.board.y + self.board.sy // 2,
            "o",
            1
        )
        
        # Makes the x value fit in a 2x1 grid
        possible_x = [i for i in range(self.board.x, self.board.sx + self.board.x, 2)]
        
        self.fruit = Fruit(
            self.scr,
            self.board.x + self.board.sx // 2 + 2,
            self.board.y + self.board.sy // 2,
            possible_x,
            "*",
            2
        )

    def gameover(self):
        self.player.restart(self.board)
        self.fruit.restart(self.board, self.player.body_coordinates)
        self.board.score = 0

    def Update(self):
        self.player.x += self.player.vx
        self.player.y += self.player.vy

        self.player.get_coordinates_body()
        

        # Collision: Player head x Player body
        for body_part in self.player.body:
            if (    self.player.x == body_part[0] and
                    self.player.y == body_part[1]):
                self.gameover()
        
        # Insert new head
        self.player.body.insert(0, (self.player.x, self.player.y))
        
        # Collision: Player head x Fruit
        if (    self.player.x == self.fruit.x and
                self.player.y == self.fruit.y):
            self.fruit.restart(self.board, self.player.body_coordinates)
            self.board.score += 1
        else:
            self.player.body.pop()
        
        # Collision: Player x Board
        if (    self.player.x <= self.board.x - 1 or # Left
                self.player.x >= self.board.x + self.board.sx or # Right
                self.player.y <= self.board.y - 1 or # Up
                self.player.y >= self.board.y + self.board.sy): # Down
            self.gameover()

        if self.board.score == self.board.max_score:
            self.state = False

        key = self.scr.getch()
        
        self.player.input(key)
        
        if key == self.KEYS["q"]:
            self.state = False

    
    def Render(self):
        self.scr.erase()
        
        self.board.render()
        self.player.render()
        self.fruit.render()

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
