import curses as cs

class Student:
    def __init__(self):
        self.__id=""
        self.__name=""
        self.__dob=""
        self.__GPA=0

    def input(self):
        self.__id=input("The student's ID: ")
        self.__name=input("The student's name: ")
        self.__dob=input("The student's DOB: ")
    def input_curses(self,stdscr):
        cs.echo()
        stdscr.addstr(3,2,"The student's ID:                                ")
        self.__id=stdscr.getstr(3,2+len("The student's ID: ")).decode("utf-8")
        stdscr.addstr(4,2,"The student's name:                              ")
        self.__name=stdscr.getstr(4,2+len("The student's name: ")).decode("utf-8")
        stdscr.addstr(5,2,"The student's DOB:                               ")
        self.__dob=stdscr.getstr(5,2+len("The student's DOB: ")).decode("utf-8")
        cs.noecho()
        stdscr.refresh()

    def __str__(self):
        return f"{self.__id} - {self.__name} - {self.__dob}"