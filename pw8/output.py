def outputMark(markmanager,stdscr):
    while True:
        cont=markmanager.displayMarks_curses(stdscr)
        if cont=="N":
            break
    markmanager.setGPAlist()
    markmanager.sortGPAlist_curses(stdscr)