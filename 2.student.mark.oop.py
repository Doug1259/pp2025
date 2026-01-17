# OOP version

class Student:
    def __init__(self):
        self.__id=""
        self.__name=""
        self.__dob=""
    def input(self):
        self.__id=input("The student's ID: ")
        self.__name=input("The student's name: ")
        self.__dob=input("The student's DOB: ")
    def __str__(self):
        return f"{self.__id} - {self.__name} - {self.__dob}"

class Course:
    def __init__(self):
        self.__id=""
        self.__name=""
    def input(self):
        self.__id=input("The course's ID: ")
        self.__name=input("The course's name: ")
    def __str__(self):
        return f"{self.__id} - {self.__name}"
    
class MarkManager:
    def __init__(self):
        self.__students=[]
        self.__courses=[]
        self.__marklist={}
    def setStudentList(self):
        ns=int(input("Enter the number of students: "))
        for i in range(ns):
            print(f"Student {i+1}")
            s=Student()
            s.input()
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
    def setMarkList(self):
        choosecourse=int(input("Select the course to mark the students: "))
        while(choosecourse>len(self.__marklist["Courses"]) or choosecourse<=0):
            print("That course is invalid, please try again")
            choosecourse=int(input("Select the course: "))
        key=str(choosecourse)
        print(f"Course choosen: {self.__marklist["Courses"][choosecourse-1]}")
        temp=[]
        for i in self.__marklist["Students"]:
            mark=float(input(f"Mark for {i}: "))
            temp.append(mark)
        self.__marklist[key]=temp
        cont=input("Do you want to continue grading the students[Y/N]: ")
        return cont

    def displayStudents(self):
        print("All the students in this class are: ")
        n=1
        for i in self.__students:
            print(f"{n}. {i}")
            n+=1
    def displayCourses(self):
        print("All the courses in this class are: ")
        n=1
        for i in self.__courses:
            print(f"{n}. {i}")
            n+=1
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

m = MarkManager()
m.setStudentList()
m.setCourseList()
m.displayStudents()
m.displayCourses()

while True:
    cont=m.setMarkList()
    if cont == "N":
        break
while True:
    cont=m.displayMarks()
    if cont == "N":
        break

