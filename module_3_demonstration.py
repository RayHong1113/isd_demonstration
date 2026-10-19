"""This module is used to demonstrate concepts from module 3."""

from decimal import Decimal

from student.student import Student
from student.college_student import CollegeStudent
from patterns.singleton.student_number_generator import StudentNumberGenerator

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

def get_students() -> list[Student]:
    """Returns a list of students.
    
    Returns:
        list[Student]: A list of students.
    """

    students = []

    students.append(CollegeStudent("John Brunelle", Decimal('1.49')))
    students.append(CollegeStudent("Elizabeth Sinclair", Decimal('.94')))
    students.append(CollegeStudent("Angela Brock", Decimal('2.61')))
    students.append(CollegeStudent("Robert Flammand", Decimal('2.51')))
    students.append(CollegeStudent("Arthur Armstrong", Decimal('2.58')))
    students.append(CollegeStudent("Chris Mullin", Decimal('3.52')))
    students.append(CollegeStudent("Jackie Blanchard", Decimal('2.6')))
    students.append(CollegeStudent("George Shanahan", Decimal('3.0')))
    students.append(CollegeStudent("Linda Eck", Decimal('3.82')))
    students.append(CollegeStudent("Judy Gardener", Decimal('4.02')))
    students.append(CollegeStudent("Donna Smith", Decimal('4.14')))
    students.append(CollegeStudent("Eric Best", Decimal('1.38')))

    return students

def main():
    """The main entry point of the program."""

    generator = StudentNumberGenerator()
    print(type(generator))
    print(id(generator))

    donkey = StudentNumberGenerator()
    print(type(donkey))
    print(id(donkey))

    students = get_students()
    
    for student in students:
        # Student numbers are unique
        print(f"{student}")

if __name__ == "__main__":
    main()
