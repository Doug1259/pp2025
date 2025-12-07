def getNumStudent():
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
        
print(marklist)