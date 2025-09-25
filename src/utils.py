from curses import color_pair


def addstr(scr, x: int, y: int, string: str, color=0) -> None:
    scr.addstr(y, x, string, color_pair(color))

def drawRectFrame(scr, x: int, y: int, sx: int, sy: int, strings: dict, color=0) -> None:
    addstr(scr, x, y, strings["border"], color)
    for i in range(x + 2, sx + x - 1, 2):
        addstr(scr, i, y, strings["horizontal"], color)
    addstr(scr, sx + x -1 , y, strings["border"], color)
    
    for j in range(y + 1, sy + y - 1):
        addstr(scr, x, j, strings["vertical"], color)
        addstr(scr, sx + x - 1, j, strings["vertical"], color)

    addstr(scr, x, y + sy - 1, strings["border"], color)
    for i in range(x + 2, sx + x - 1, 2):
        addstr(scr, i, y + sy - 1, strings["horizontal"], color)
    addstr(scr, sx + x - 1 , y + sy - 1, strings["border"], color)


def drawRect(scr, x: int, y: int, sx: int, sy: int, string: str, color=0) -> None:
    """ Draw a full rectangle
        * A coordenada em x tem que ser: (x * 2) - 1
    """
    for j in range(y, sy + y):
        for i in range(x, sx + x, 2):
            addstr(scr, i, j, string, color)
