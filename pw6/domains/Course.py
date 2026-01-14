import curses as cs

class Course:
    def __init__(self):
        self.__id=""
        self.__name=""
        self.__credits=0
        
    def input(self):
        self.__id=input("The course's ID: ")
        self.__name=input("The course's name: ")
        self.__credits=int(input("The course's credits: "))
    def input_curses(self,stdscr):
        cs.echo()
        stdscr.addstr(3,2,"The course's ID:                                ")
        self.__id=stdscr.getstr(3,2+len("The course's ID: ")).decode("utf-8")
        stdscr.addstr(4,2,"The course's name:                              ")
        self.__name=stdscr.getstr(4,2+len("The course's name: ")).decode("utf-8")
        stdscr.addstr(5,2,"The course's credits:                               ")
        self.__credits=int(stdscr.getstr(5,2+len("The course's credits: ")).decode("utf-8"))
        cs.noecho()
        stdscr.refresh()

    def __str__(self):
        return f"{self.__id} - {self.__name}: {self.__credits} credit(s)"
    
    def getcredits(self):
        return self.__credits
    def getname(self):
        return self.__name
    def getid(self):
        return self.__id 
    
    def setcredits(self,newcredits):
        self.__credits=newcredits
    def setname(self,newname):
        self.__name=newname
    def setid(self,newid):
        self.__id=newid