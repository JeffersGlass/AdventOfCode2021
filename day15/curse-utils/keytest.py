import curses

screen = curses.initscr()
screen.keypad(True)

while True:
    c = screen.getch()
    if c == 8: exit() #backspace to quit
    screen.addstr(0,0,"       ")
    screen.addstr(0,0,str(c))