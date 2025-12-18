from input import inputMark
from output import outputMark
from domains import MarkManager
import curses as cs

def main(stdscr):
    stdscr.clear()
    mm=MarkManager.initClass()
    inputMark(mm,stdscr)
    outputMark(mm,stdscr)
    stdscr.refresh()
cs.wrapper(main)