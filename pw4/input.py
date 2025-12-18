def inputMark(markmanager,stdscr):
    markmanager.setStudentList_curses(stdscr)
    markmanager.setCourseList_curses(stdscr)
    while True:
        cont=markmanager.setMarkList_curses(stdscr)
        if cont=="N":
            break
    markmanager.setGPAlist()