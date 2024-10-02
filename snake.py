import curses

from Player import Player
from Apple import Apple

# TODO Fazer um método render no objeto Apple
# TODO O Player nake sai andando por ai, arrumar isso


class Game:
    def __init__(self):
        self.stdscr = curses.initscr() # Inicia a janela
        self.stdscr.nodelay(True) # Se não tiver input o padrão é -1
        
        # Set color
        curses.start_color()
        curses.use_default_colors()

        curses.noecho() # Não exibe os inputs
        curses.curs_set(0) # Não mostra o cursor
       
        # Color pairs
        curses.init_pair(1, 2, -1) # Green 
        curses.init_pair(2, 3, -1) # Yellow
        curses.init_pair(3, 4, -1) # Blue
        
        self.state = True
        
        self.KEYS = {"q": 113}
        self.TICKRATE = 500
        
        self.cols, self.rows = self.stdscr.getmaxyx()
        self.player = Player(self.stdscr,
                      [(self.rows//2, self.cols//2)],
                      3,
                      2,
                      "*",
                      1)

        self.apple = Apple(self.stdscr,
                           self.rows//2 - 18,
                           self.cols//2,
                           3,
                           2,
                           "*",
                           2)
    

    def Update(self):
        self.player.update(self.apple.score)
        
        if (    self.player.body[0][0] == self.apple.x and
                self.player.body[0][1] == self.apple.y):
            self.apple.reset(self.rows, self.cols)
        key = self.stdscr.getch()
        
        self.player.input(key)
        
        if key == self.KEYS["q"]:
            self.state = False

    
    def Render(self):
        self.stdscr.erase()

        self.player.render()
        self.apple.render()

        self.stdscr.refresh()


    def Loop(self, stdscr):
        while self.state:
            self.Update()
            self.Render()

            curses.flushinp() # Faz com que os inputs não se "arrastem"
            curses.napms(self.TICKRATE)


if __name__ == "__main__":
    game = Game()
    curses.wrapper(game.Loop)
