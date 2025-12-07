"""def getNumStudent():
    n=int(input("Enter the number of students in a class: "))
    return n
def getStudentInfo():
    id=input("The student's id: ")
    name=input("The student's name: ")
    dob=input("The students'DoB: ")
    info=id+"-"+name+"-"+dob
    return info

def getNumCourse():
    n=int(input("Enter the number of courses: "))
    return n
def getCourseInfo():
    id=input("The course's id: ")
    name=input("The course's name: ")
    info=id+"-"+name
    return info

def getMark(course,student,marklist):
    choosecourse=int(input("Select the course (please enter an integer >= 1): "))
    while(choosecourse<=0 or choosecourse>len(course)):
        print("That course is invalid, please try again")
        choosecourse=int(input("Select the course: "))
    print(f"Course: {course[choosecourse-1]}")
    temp=[]
    for i in student:
        mark=int(input(f"Enter {i} 's mark: "))
        temp.append(mark)
    index=str(choosecourse)
    marklist[index]=temp
    cont=input("Do you want to continue marking the student[Y/N]: ")
    return cont

def listStudent(studentlist):
    print("All the students in this class are:")
    n=1
    for i in studentlist:
        print(f"{n}. {i}")
        n+=1
def listCourse(courselist):
    print("All the courses in this class are:")
    n=1
    for i in courselist:
        print(f"{n}. {i}")
        n+=1
def listMark(marklist):
    choosecourse=int(input("Select the course to view the marks (please enter an integer >= 1): "))
    while(choosecourse>len(marklist["Courses"]) or choosecourse<=0):
        print("That course is invalid, please try again")
        choosecourse=int(input("Select the course: "))
    print(f"The marks for course: {marklist["Courses"][choosecourse-1]}")
    index=str(choosecourse)
    n=0
    for i in studentlist: 
        print(f"{i} 's mark: {marklist[index][n]}")
        n+=1
    cont=input("Do you want to continue viewing the marks[Y/N]: ")
    return cont    

#

studentlist=[]
courselist=[]
marklist={}

ns=getNumStudent()
print("Enter the students info: ")
for i in range(1,ns+1):
    print(f"Student {i}")
    studentlist.append(getStudentInfo())
marklist["Students"]=studentlist
listStudent(studentlist)

nc=getNumCourse()
print("Enter the courses info: ")
for i in range(1,nc+1):
    print(f"Course {i}")
    courselist.append(getCourseInfo())
marklist["Courses"]=courselist
listCourse(courselist)

cont=True
while cont==True:
    temp = getMark(courselist,studentlist,marklist)
    if temp == "N":
        cont = False 
cont=True
while cont==True:
    temp = listMark(marklist)
    if temp == "N":
        cont = False
        
print(marklist)"""

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

