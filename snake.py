import curses

from Snake import Snake
from Apple import Apple

# TODO Fazer um método render no objeto Apple
# TODO A Snake sai andando por ai, arrumar isso


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
        curses.init_pair(2, 1, -1) # Yellow
        curses.init_pair(3, 4, -1) # Blue
        
        self.state = True
        
        self.KEYS = {"q": 113}
        self.TICKRATE = 50
        
        self.cols, self.rows = self.stdscr.getmaxyx()
        self.snake = Snake(self.stdscr,
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
                           "o",
                           2)
        
    

    def Update(self):
        self.snake.update(self.apple.score)

        key = self.stdscr.getch()
        
        self.snake.input(key)
        
        if key == self.KEYS["q"]:
            self.state = False

    
    def Render(self):
        self.stdscr.erase()

        self.snake.render()
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
