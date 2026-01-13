import zipfile as zf
import os

def inputMark(markmanager,stdscr):
    markmanager.setStudentList_curses(stdscr)
    markmanager.displayStudents_curses(stdscr,7)

    markmanager.setCourseList_curses(stdscr)
    markmanager.displayCourses_curses(stdscr,7)

    markmanager.setMarkList_curses(stdscr)
    
    zip_path = "./students.zip"
    students_data = "./students.txt"
    courses_data = "./courses.txt"
    marks_data = "./marks.txt"
    with zf.ZipFile(zip_path,'w',zf.ZIP_DEFLATED) as zip:
        zip.write(students_data)
        zip.write(courses_data)
        zip.write(marks_data)
    os.remove("students.txt")
    os.remove("courses.txt")
    os.remove("marks.txt")