"""This module defines the StudentNumberGenerator class."""

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class StudentNumberGenerator:
    """ A class to model a singleton"""

    __instance = None
    __next_student_number: int = 20_240_000

    def __new__(cls):
        """returns the single instance of the 
        singleton manager class
        """
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    @staticmethod
    def get_instance() -> StudentNumberGenerator:
        """gets the instance of the StudentManagerGenerator"""

        if not StudentNumberGenerator.__instance:
            StudentNumberGenerator.__instance = StudentNumberGenerator()
        
        return StudentNumberGenerator.__instance

    def get_next_student_number(self):
        """returns the next available 
        unique student number

        Returns:
            int: the next available unique student
            number
        """
        next_student_number = self.get_next_student_number
        self.__next_student_number += 1
        return next