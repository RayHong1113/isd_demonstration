"""This module defines the VolunteerDecorator class."""

from decimal import Decimal
from student.student import Student
from patterns.decorator.student_decorator import StudentDecorator

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class VolunteerDecorator(StudentDecorator):
    """
     Represent the a decorator for a student
    """
    def __init__(self, student: Student) -> None:
        """
            Initialize a new instance of the StudentDecorator
        """
        super().__init__(student)

    def get_grade_point_average(self) -> Decimal:
        """Returns the GPA of a student who volunteers
        
            Students who volunteer get a 0.25 increase to their 
            gpa

            Returns:
                Decimal: The gpa of the student who volunteers
        """
        GPA_POINT_AVERAGE_INCREASE = Decimal('.25')

        return min((super().get_grade_point_average() + GPA_POINT_AVERAGE_INCREASE, Decimal('4.5')))
        
        