class NoSuchCourseError(Exception):
    def __init__(self):
        self.msg= "There is no such course!"
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.courses = self.Courses()

    class Courses:
        def __init__(self):
            self.enrolled_courses = []

        def enroll_course(self, course):
            if course not in self.enrolled_courses:
                self.enrolled_courses.append(course)
                print(f"{course} enrolled successfully.")
            else:
                print(f"You are already enrolled in {course}.")

        def disenroll_course(self, course):
            if course in self.enrolled_courses:
                self.enrolled_courses.remove(course)
                print(f"{course} disenrolled successfully.")
            else:
                print(f"You are not enrolled in {course}.")

        def display_courses(self):
            if self.enrolled_courses:
                print("Enrolled Courses:")
                for course in self.enrolled_courses:
                    print("-", course)
            else:
                print("No courses enrolled.")
students= dict()
c=0
while True:
    print("1) Add a courses to a student\n2) Disenroll a student from a course\n3) Display the existing students with courses\n4) Exit")
    ch= int(input("Enter your choice: "))
    if ch==1:
        c+=1
        name= input("Enter the name of student: ")
        roll= input("Enter the roll no.: ")
        student= Student(name, roll)
        avail_courses= {'23AI201': 'Machine Learning', '23DS224': 'Data Scavenging', '23BT231': 'Bitcoin and NFT'}
        for i in avail_courses.keys():
            print(f'{i} - {avail_courses[i]}')
        try:
            ch= input("Enter the course you want to enroll into (using the course code): ")
            if ch not in avail_courses.keys():
                raise NoSuchCourseError()
            student.courses.enroll_course(ch)
        except NoSuchCourseError as nsce:
            print(nsce.msg)
        students[roll]= student
    elif ch==2:
        for i in students.keys():
            print(f"{i} - {students[i].name}")
            students[i].courses.display_courses()
    elif ch==3:
        for i in students.keys():
            print(f"{i}- {students[i].name}")
        roll= input("Enter the roll number of the student: ")
        if roll in students.keys():
            students[roll].courses.display_courses()


