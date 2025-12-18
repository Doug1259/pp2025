def outputMark(markmanager,stdscr):
    markmanager.displayStudents_curses(stdscr)
    markmanager.displayCourses_curses(stdscr)
    while True:
        cont=markmanager.displayMarks_curses(stdscr)
        if cont=="N":
            break
    markmanager.sortGPAlist_curses(stdscr)