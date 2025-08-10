
import curses

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    vending_machine_ascii = r"""
    ______________________
    |   [VENDING MACHINE]  |
    |   [1] Lemon Dou      |
    |   [2] Peach Lemon    |
    |   [3] Devil Lemon    |
    |______________________|
    """

    options = [
        "1. Buy Drink",
        "2. Restock",
        "3. Show Cards",
        "4. Remove Column",
        "5. Exit"
    ]

    selected = -1
    while True:
        stdscr.clear()
        stdscr.addstr(vending_machine_ascii)

        for i, opt in enumerate(options, start=1):
            stdscr.addstr(6 + i, 0, opt)

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            selected = 1
        elif key == ord('2'):
            selected = 2
        elif key == ord('3'):
            selected = 3
        elif key == ord('4'):
            selected = 4
        elif key == ord('5'):
            break

        if selected != -1:
            stdscr.addstr(17, 0, f"You selected option {selected}")
            stdscr.refresh()
            stdscr.getch()
            selected = -1

curses.wrapper(main)