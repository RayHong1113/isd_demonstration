"""This module is used to demonstrate concepts from module 1."""

from course.course import Course
from course.department import Department

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

def main():
    """The main entry point of the program."""
    try:
        course = Course("COMP-2327 ISD",Department.COMPUTER_SCIENCE, 90)
        
        print(f"Course: {course}")
    
        print(f"Course name: {course.name}")
        

    
        print(f"Original Credit Hours: {course.credit_hours}")
        course.credit_hours = 45
        print(f"After Credit Hours: {course.credit_hours}")

        print(course.name)
        print(course.department)
        print(course.credit_hours)


    
    except AttributeError as error:
        print(error)
    


if __name__ == "__main__":
    main()
