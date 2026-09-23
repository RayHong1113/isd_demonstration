""""This module define the course class"""

__author__ ="ACE Faculty"
__version__ ="1.0.0"

from abc import ABC, abstractmethod
from course.department import Department
from course.student import Student


class Course(ABC):
    """Represents a course at a post secondary institution"""

    ENROLLMENT_LIMIT = 30
    """The maximum number of students enrolled in course""" 

    def __init__(
            self,
            name: str,
            department: Department,
            credit_hours: int): 
        """Represents a course at an education institution"""

        self.__students = []

        """Initializes the new instance of the course class.
        
            Args:
                name (str) : the name of the course
                department (Department) : The department that the course comes from
                credit_hours (int) : number of credit hours

            Raises:
                ValueError : Raised when incorrect args are provided
        """

        if len(name.strip()) == 0:
            raise ValueError("name cannot be an empty string")

        if isinstance(credit_hours, int):
            if credit_hours <= 0:
                raise ValueError("credit_hours must be a value greater than zero")
            else:
                self.credit_hours = credit_hours # call the setter directly

        self.__name = name.strip() 
        self.__department = department
       

    @property
    def name(self) -> str:
        """Gets the name of the course

            Returns:
                str: The name of the course
        
        """
        return self.__name

    @property
    def department(self)->int:
        return self.__department

    @property
    def credit_hours(self)-> int:
        return self.__credit_hours

    @credit_hours.setter
    def credit_hours(self,credit_hours:int) -> None:
        if credit_hours <= 0:
            raise ValueError("credit_hours must be a value greater than zero") 
        self.__credit_hours = credit_hours

    @property
    def students(self) -> list[Student]:
        """Gets the students enrolled in course.
        
            Returns: 
                list[Student] : The students enrolled in the course. 
        """
        return self.__students

    @abstractmethod
    def enroll_student(self, student: Student)-> None:
        """Enrolls the student in the course. 

            Args:
                student (Student) : The student being enrolled in the course.
        """
        pass

    def __str__(self)->str:
        return (f"Course: {self.__name.title()}\n"
                f"Department: {self.__department.name.replace('_',' ').title()}\n"
                f"Credit Hours: {self.__credit_hours}")



