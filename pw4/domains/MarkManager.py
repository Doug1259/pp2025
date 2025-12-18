import math
import numpy as np
import curses as cs
from .Student import Student
from .Course import Course

class MarkManager:
    def __init__(self):
        self.__students=[]
        self.__courses=[]
        self.__marklist={}
        self.__gpa=[]


    def setStudentList(self):
        ns=int(input("Enter the number of students: "))
        for i in range(ns):
            print(f"Student {i+1}")
            s=Student()
            s.input()
            self.__students.append(s)
        self.__marklist["Students"]=self.__students
    def setStudentList_curses(self,stdscr):
        stdscr.clear()
        stdscr.addstr(1,1,"Enter the number of students: ")
        cs.echo()
        ns=int(stdscr.getstr(1,1+len("Enter the number of students: ")).decode("utf-8"))
        cs.noecho()
        stdscr.refresh()
        for i in range(ns):
            stdscr.addstr(2,1,f"Student {i+1}")
            s=Student()
            s.input_curses(stdscr)
            self.__students.append(s)
        self.__marklist["Students"]=self.__students

    def setCourseList(self):
        nc=int(input("Enter the number of courses: "))
        for i in range(nc):
            print(f"Course {i+1}")
            c=Course()
            c.input()
            self.__courses.append(c)
        self.__marklist["Courses"]=self.__courses
    def setCourseList_curses(self,stdscr):
        stdscr.clear()
        stdscr.addstr(1,1,"Enter the number of courses: ")
        cs.echo()
        nc=int(stdscr.getstr(1,1+len("Enter the number of courses: ")).decode("utf-8"))
        cs.noecho()
        stdscr.refresh()
        for i in range(nc):
            stdscr.addstr(2,1,f"Course {i+1}")
            c=Course()
            c.input_curses(stdscr)
            self.__courses.append(c)
        self.__marklist["Courses"]=self.__courses

    def setMarkList(self):
        choosecourse=int(input("Select the course to mark the students: "))
        while(choosecourse>len(self.__marklist["Courses"]) or choosecourse<=0):
            print("That course is invalid, please try again")
            choosecourse=int(input("Select the course: "))
        key=str(choosecourse)
        print(f"Course choosen: {self.__marklist["Courses"][choosecourse-1]}")
        temp=[]
        for i in self.__marklist["Students"]:
            mark=math.floor(float(input(f"Mark for {i}: "))*10)/10
            temp.append(mark)
        self.__marklist[key]=temp
        cont=input("Do you want to continue grading the students[Y/N]: ")
        return cont
    def setMarkList_curses(self,stdscr):
        stdscr.clear()
        stdscr.addstr(1,1,"Select the course to mark the students: ")
        cs.echo()
        choosecourse=int(stdscr.getstr(1,1+len("Select the course to mark the students: ")).decode("utf-8"))
        cs.noecho
        stdscr.refresh()
        while(choosecourse>len(self.__marklist["Courses"]) or choosecourse<=0):
            stdscr.clear()
            stdscr.addstr(2,1,"That course is invalid, please try again")
            stdscr.addstr(1,1,"Select the course to mark the students: ")
            cs.echo()
            choosecourse=int(stdscr.getstr(1,1+len("Select the course to mark the students: ")).decode("utf-8"))
            cs.noecho()
            stdscr.refresh()
        key=str(choosecourse)
        stdscr.addstr(2,1,f"Course choosen: {self.__marklist["Courses"][choosecourse-1]}        ")
        n=2
        temp=[]
        for i in self.__marklist["Students"]:
            stdscr.addstr(n+1,2,f"Mark for {i}: ")
            cs.echo()
            mark=math.floor(float(stdscr.getstr(n+1,3+len(f"Mark for{i}: ")).decode("utf-8"))*10)/10
            cs.noecho()
            stdscr.refresh()
            temp.append(mark)
            n+=1
        self.__marklist[key]=temp
        stdscr.addstr(n+2,1,"Do you want to continue grading the students[Y/N]:")
        cont=""
        while True:
            cs.echo()
            cont=stdscr.getstr(n+2,1+len("Do you want to continue grading the students[Y/N]: ")).decode("utf-8")
            cs.noecho()
            stdscr.refresh()
            if (cont == "Y" or cont =="N"):
                break
        return cont


    def setGPAlist(self):
        nc=0
        ns=0
        for course in self.__marklist["Courses"]:
            nc+=1
        for studnet in self.__marklist["Students"]:
            ns+=1
        index=0
        marks=np.zeros(shape=(nc,ns))
        credits=np.zeros(shape=(1,nc))
        for course in self.__marklist["Courses"]:
            key=str(index+1)
            if(self.__marklist[key]!=None):
                marks[index]=self.__marklist[key]
                credits[0,index]=self.__courses[index].getcredits()
            index+=1
        index=0
        total_marks=np.zeros(shape=(nc,ns))
        for course in self.__marklist["Courses"]:
            total_marks[index]=np.multiply(marks[index],credits[0,index])
            index+=1
        total_marks=np.sum(total_marks,axis=0)
        total_credits=np.sum(credits)
        self.__gpa=np.divide(total_marks,total_credits)

    def sortGPAlist(self):
        keys=[str(student) for student in self.__students]
        values=[math.floor(i*10)/10 for i in self.__gpa]
        sorted_value_index=np.flip(np.argsort(values))
        sorted_gpa={keys[i]: values[i] for i in sorted_value_index}
        sorted_gpa_keys=list(sorted_gpa.keys())
        sorted_gpa_values=list(sorted_gpa.values())
        print("The students' gpa in descending order: ")
        n=1
        for i in sorted_gpa:
            print(f"{n}. {sorted_gpa_keys[n-1]}: {sorted_gpa_values[n-1]}")
            n+=1
    def sortGPAlist_curses(self,stdscr):
        keys=[str(student) for student in self.__students]
        values=[math.floor(i*10)/10 for i in self.__gpa]
        sorted_value_index=np.flip(np.argsort(values))
        sorted_gpa={keys[i]: values[i] for i in sorted_value_index}
        sorted_gpa_keys=list(sorted_gpa.keys())
        sorted_gpa_values=list(sorted_gpa.values())
        stdscr.clear()
        stdscr.addstr(1,1,"The students' gpa in descending order: ")
        n=1
        for i in sorted_gpa:
            stdscr.addstr(n+1,2,f"{n}. {sorted_gpa_keys[n-1]}: {sorted_gpa_values[n-1]}")
            n+=1
        stdscr.addstr(n+2,1,"Press any key to continue")
        stdscr.getch()
        stdscr.refresh()


    def displayStudents(self):
        print("All the students in this class are: ")
        n=1
        for i in self.__students:
            print(f"{n}. {i}")
            n+=1
    def displayStudents_curses(self,stdscr):
        stdscr.clear()
        stdscr.addstr(1,1,"All the students in this class are: ")
        n=1
        for i in self.__students:
            stdscr.addstr(n+1,2,f"{n}. {i}")
            n+=1
        stdscr.addstr(n+2,1,"Press any key to continue")
        stdscr.getch()
        stdscr.refresh()

    def displayCourses(self):
        print("All the courses in this class are: ")
        n=1
        for i in self.__courses:
            print(f"{n}. {i}")
            n+=1
    def displayCourses_curses(self,stdscr):
        stdscr.clear()
        stdscr.addstr(1,1,"All the courses in this class are: ")
        n=1
        for i in self.__courses:
            stdscr.addstr(n+1,2,f"{n}. {i}")
            n+=1
        stdscr.addstr(n+2,1,"Press any key to continue")
        stdscr.getch()
        stdscr.refresh()

    def displayMarks(self):
        choosecourse=int(input("Select the course to view the students' mark: "))
        while(choosecourse>len(self.__marklist["Courses"]) or choosecourse<=0):
            print("That course is invalid, please try again")
            choosecourse=int(input("Select the course: "))
        key=str(choosecourse)
        print(f"The marks for course: {self.__marklist["Courses"][choosecourse-1]}")
        n=1
        for i in self.__marklist["Students"]:
            print(f"{n}. {i}: {self.__marklist[key][n-1]}")
            n+=1
        cont=input("Do you want to continue viewing the marks[Y/N]: ")
        return cont
    def displayMarks_curses(self,stdscr):
        stdscr.clear()
        stdscr.addstr(1,1,"Select the course to view the students' mark: ")
        cs.echo()
        choosecourse=int(stdscr.getstr(1,1+len("Select the course to view the students' mark: ")).decode("utf-8"))
        cs.noecho
        stdscr.refresh()
        while(choosecourse>len(self.__marklist["Courses"]) or choosecourse<=0):
            stdscr.clear()
            stdscr.addstr(2,1,"That course is invalid, please try again")
            stdscr.addstr(1,1,"Select the course to view the students' mark: ")
            cs.echo()
            choosecourse=int(stdscr.getstr(1,1+len("Select the course to view the students' mark: ")).decode("utf-8"))
            cs.noecho()
            stdscr.refresh()
        key=str(choosecourse)
        stdscr.addstr(2,1,f"Course choosen: {self.__marklist["Courses"][choosecourse-1]}        ")
        n=1
        for i in self.__marklist["Students"]:
            stdscr.addstr(n+2,2,f"{n}. {i}: {self.__marklist[key][n-1]}")
            n+=1
        stdscr.addstr(n+3,1,"Do you want to continue viewing the marks[Y/N]:")
        cont=""
        while True:
            cs.echo()
            cont=stdscr.getstr(n+3,1+len("Do you want to continue viewing the marks[Y/N]: ")).decode("utf-8")
            cs.noecho()
            stdscr.refresh()
            if (cont == "Y" or cont =="N"):
                break
        return cont

def initClass():
    mm=MarkManager()
    return mm