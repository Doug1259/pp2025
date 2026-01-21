from input import inputMark
from output import outputMark
from domains import MarkManager
import curses as cs

def main(stdscr):
    mm=MarkManager.initClass()
    while True:
        stdscr.clear()
        stdscr.addstr(1,1,"--------------- Student Mark Manager ---------------")
        stdscr.addstr(2,1,"1. Create or overwrite data")
        stdscr.addstr(3,1,"2. Check for and load existing data")
        stdscr.addstr(4,1,"3. Exit the program")
        option=stdscr.getch()
        while option not in (49,50,51):
            option=stdscr.getch()
        if(option==49):
            stdscr.clear()
            stdscr.addstr(1,1,"Attention! if there is any existing data, it will be overwritten")
            stdscr.addstr(3,1,"Do you want to continue [Y/N]: ")
            option=stdscr.getkey()
            while option not in ("Y","N","y","n"):
                option=stdscr.getkey()
            if option in ("Y","y"):
                stdscr.clear()
                inputMark(mm,stdscr)
                outputMark(mm,stdscr)
                stdscr.refresh()
                break
            else:
                continue
            stdscr.refresh()
        elif(option==50):
            found=mm.loaddata_pickle()
            if found==False:
                stdscr.clear()
                stdscr.addstr(1,1,"There is no existing data")
                stdscr.addstr(3,1,"Press any key to return")
                stdscr.getch()
                stdscr.refresh()
                continue
            else:
                stdscr.clear()
                mm.displayStudents_curses(stdscr,1)
                stdscr.clear()
                mm.displayCourses_curses(stdscr,1)
                outputMark(mm,stdscr)
                break
        else:
            break
        stdscr.refresh()      
cs.wrapper(main)