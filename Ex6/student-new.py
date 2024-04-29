class NoSuchCourseError(Exception):
    def __init__(self, name):
        self.msg = f"There is no course with name {name}"

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.courses = self.Courses()

    class Courses:
        def __init__(self):
            self.enrolled_courses = []

        def enroll(self, *course_codes):
            for code in course_codes:
                self.enrolled_courses.append(code)
                print(f"{code} enrolled successfully.")

        def disenroll(self, course):
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
    def __del__(self):
            print(f"Student object {self.name} cleared from memeory.")

students = {}

while True:
    print("1) Add a student and enroll in one or more courses")
    print("2) Disenroll a student from a course")
    print("3) Display the existing students with courses")
    print("4) Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter the name of student: ")
        roll = input("Enter the roll no.: ")
        student = Student(name, roll)
        avail_courses = {'23BS201': 'Maths', '23BS202': 'Physics', '23BS203': 'Chemistry', '23CS251': 'Python'}
        print("Available Courses:")
        for code, course_name in avail_courses.items():
            print(f'{code} - {course_name}')

        course_codes = input("Enter the course codes you want to enroll into (separated by space): ").split()
        for code in course_codes:
            try:
                if code in avail_courses.keys():
                    student.courses.enroll(code)
                else:
                    raise NoSuchCourseError(code)
            except NoSuchCourseError as nsce:
                print(nsce.msg)

        students[roll] = student

    elif choice == 2:
        roll = input("Enter the roll number of the student: ")
        if roll in students.keys():
            student = students[roll]
            student.courses.display_courses()
            course_code = input("Enter the course code you want to disenroll from: ")
            student.courses.disenroll(course_code)

    elif choice == 3:
        for roll, student in students.items():
            print(f"Roll No: {roll}, Name: {student.name}")
            student.courses.display_courses()

    elif choice == 4:
        print("Quitting....")
        break