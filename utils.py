from curses import color_pair


def addstr(scr, x: int, y: int, ch: str, color=0):
    scr.addstr(y, x, ch, color_pair(color))

def drawRectFrame(scr, x: int, y: int, sx: int, sy: int, ch: dict, color=0):
    addstr(scr, x, y, ch["border"], color)
    for i in range(x + 2, sx + x - 1, 2):
        addstr(scr, i, y, ch["horizontal"], color)
    addstr(scr, sx + x -1 , y, ch["border"], color)
    
    for j in range(y + 1, sy + y - 1):
        addstr(scr, x, j, ch["vertical"], color)
        addstr(scr, sx + x - 1, j, ch["vertical"], color)

    addstr(scr, x, y + sy - 1, ch["border"], color)
    for i in range(x + 2, sx + x - 1, 2):
        addstr(scr, i, y + sy - 1, ch["horizontal"], color)
    addstr(scr, sx + x - 1 , y + sy - 1, ch["border"], color)


def drawRect(scr, x: int, y: int, sx: int, sy: int, ch: str, color=0):
    """ Draw a full rectangle
        * A coordenada em x tem que ser: (x * 2) - 1
    """
    for j in range(y, sy + y):
        for i in range(x, sx + x, 2):
            addstr(scr, i, j, ch, color)
