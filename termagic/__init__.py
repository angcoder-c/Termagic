'''
from curses import wrapper, error
import os
os.system('cls' if os.name == 'nt' else 'clear')

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(1, 11):
        v = i
        try:
            pass# stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
        except:
            pass
        

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
'''