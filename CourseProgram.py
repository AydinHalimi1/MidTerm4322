'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''

import CourseClass as c

def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']

    course = c.Course(name,crn,seats,status)
    course.get__name()
    course.get__crn()
    course.get__seats()
    course.get__status()
    
    for students in John:
      John = c.Register(name,crn)
      John.get_studentname()
      John.get_crn()

    for students in James:
      James = c.Register(name,crn)
      James.get_studentname()
      James.get_crn()

    for students in Jill:
      Jill = c.Register(name,crn)
      Jill.get_studentname()
      Jill.get_crn()

    for students in Jack:
      Jack = c.Register(name,crn)
      Jack.get_studentname()
      Jack.get_crn()

    for students in Joanne:
      Joanne = c.Register(name,crn)
      Joanne.get_studentname()
      Joanne.get_crn()


    print("Student Name:",course.get_studentname())
    print("Course Name:",course.get_name())
    print("CRN:",course.get_crn())
    print("Seats left:",course.get_status())

    print("Student Name:",course.get_studentname())
    print("Course Name:",course.get_name())
    print("CRN:",course.get_crn())
    print("Seats left:",course.get_status())

    print("Student Name:",course.get_studentname())
    print("Course Name:",course.get_name())
    print("CRN:",course.get_crn())
    print("Seats left:",course.get_status())

    print("Student Name:",course.get_studentname())
    print("Course Name:",course.get_name())
    print("CRN:",course.get_crn())
    print("Seats left:",course.get_status())


    if course.get__seats < len(students):
       print("Sorry",get_studentname,",","registration is closed for MIS 4322 - Advanced Python")
 
    
main()



        
    
    
