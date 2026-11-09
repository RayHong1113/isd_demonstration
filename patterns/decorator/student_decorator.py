"""This module defines the StudentDecorator class."""

from decimal import Decimal
from student.student import Student

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class StudentDecorator(Student):
    """Represents the decorator object for student"""

    def __init__(self, student: Student) -> None:
        """Initialize a new instance of Student

            Args:
                student (Student) : The student that is returned
        """
        self.__student = student

    def get_grade_point_average(self)-> Decimal:
        """Returns the student's grade average

        Returns
            Decimal: the student's grade point average
        """

        return self.__student.get_grade_point_average()

