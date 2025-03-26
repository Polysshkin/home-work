from datetime import datetime
from typing import List, Optional

class Student:
    def __init__(self, id_number: int, name: str, dob: datetime):
        self.id_number = id_number
        self.name = name
        self.dob = dob
        self.enrollments: List[Enrollment] = []
    
    def enroll(self, course, semester, semester_date):
        self.enrollments.append(Enrollment(self, course, semester, semester_date))
    
    def calculate_gpa(self, start_date: datetime, end_date: datetime) -> float:
        grades = [e.grade for e in self.enrollments if e.grade is not None and start_date <= e.semester_date <= end_date]
        return sum(grades) / len(grades) if grades else 0.0

class Professor:
    def __init__(self, id_number: int, name: str):
        self.id_number = id_number
        self.name = name
        self.courses: List[Course] = []
    
    def teach(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, id_number: int, name: str, professor: Professor):
        self.id_number = id_number
        self.name = name
        self.professor = professor
        self.students: List[Student] = []
    
    def enroll_student(self, student: Student, semester: str, semester_date: datetime):
        self.students.append(student)
        student.enroll(self, semester, semester_date)

class Enrollment:
    def __init__(self, student: Student, course: Course, semester: str, semester_date: datetime, grade: Optional[float] = None):
        self.student = student
        self.course = course
        self.semester = semester
        self.semester_date = semester_date
        self.grade = grade

class Schedule:
    def __init__(self, course: Course, time: str, room: str):
        self.course = course
        self.time = time
        self.room = room

class Administration:
    @staticmethod
    def generate_report(student: Student, start_date: datetime, end_date: datetime):
        gpa = student.calculate_gpa(start_date, end_date)
        print(f"Student Report for {student.name} (ID: {student.id_number})")
        print(f"GPA from {start_date.strftime('%Y-%m')} to {end_date.strftime('%Y-%m')}: {gpa}")
        print("Enrolled Courses:")
        for enrollment in student.enrollments:
            if start_date <= enrollment.semester_date <= end_date:
                print(
                    f"  - {enrollment.course.name} ({enrollment.semester}): Grade {enrollment.grade if enrollment.grade is not None else 'N/A'}")
