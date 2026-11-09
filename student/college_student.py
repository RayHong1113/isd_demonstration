"""This module defines the CollegeStudent class."""

from decimal import Decimal
from patterns.singleton.student_number_generator import StudentNumberGenerator

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class CollegeStudent:
    """Represents a college student."""

    def __init__(self, 
                 name: str,
                 grade_point_average: Decimal) -> None:
        """Initializes a new instance of the CollegeStudent class.
        
        Args:
            student_number (int): The student identity number.
            name (str): The student's name.
            grade_point_average (Decimal): The student's grade point
                average.

        Raises:
            ValueError: Raised when the student number is not a four
                digit positive value or the name is an empty string or 
                the grade_point_average is outside of the range 0 - 4.5.
        """

        # if student_number <= 999:
        #     raise ValueError("student_number must be four digits "
        #                      "greater than zero")
        
        if name.strip() == "":
            raise ValueError("name cannot be an empty string")
        
        if (grade_point_average < Decimal('0') or
           grade_point_average > Decimal('4.5')):
            raise ValueError("grade_point_average must be a Decimal "
                             "value between 0 and 4.5 (inclusive)")

        self.__student_number = StudentNumberGenerator.get_instance().get_next_student_number()
        self.__name = name.strip()
        self.__grade_point_average = grade_point_average
        
    @property
    def student_number(self) -> int:
        """Gets the student's identity number.
        
        Returns:
            The student's identity number.
        """

        return self.__student_number
    
    @property
    def name(self) -> str:
        """Gets the student's name.
        
        Returns:
            The student's name.
        """

        return self.__name
    
    def get_grade_point_average(self) -> Decimal:
        """Returns the student's grade point average.
        
        Returns:
            Decimal: The student's grade point average.
        """

        return self.__grade_point_average

    def set_grade_point_average(self, grade_point_average: Decimal) -> None:
        """Sets the student's grade point average.
        
        Args:
            grade_point_average (Decimal) - The new grade point average.
        """

        self.__grade_point_average = grade_point_average
    
    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string 
        representation of the object.

        Returns:
            str: The "informal" or nicely printable string 
                representation of the object.
        """

        return f"{self.name} ({self.student_number})"
