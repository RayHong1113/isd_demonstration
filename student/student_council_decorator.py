"""This module defines the StudentCouncilDecorator class."""

from decimal import Decimal

from student.student import Student
from patterns.decorator.student_decorator import StudentDecorator

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class StudentCouncilDecorator(StudentDecorator):
    """Represents a decorated object for a Student"""

    def __init__(self, student:Student) ->None:
        """Initializes a new instance of StudentCouncilDecorator class
        
            Args:
                student (Student): The student to decorate
        """
        super().__init__(student)

    def get_grade_point_average(self) -> Decimal:
        """Returns the grade point average of a student 
        tha is in student council
        
        An increase to the grade point average is based on students
        original grade point average

        Returns:
            Decimal: The GPA of the student enrolled in student council

        """
        get_grade_point_average = super().get_grade_point_average()

        increases = {
            Decimal('4.13') : Decimal('.35'),
            Decimal('3.67') : Decimal('.19'),
            Decimal('2.40') : Decimal('.04')
        }
        increase = 0 

        for average in increases:
            if increase == 0 and get_grade_point_average >= average:
                increase = increases[average]

        return min(get_grade_point_average + increase, Decimal('4.5'))