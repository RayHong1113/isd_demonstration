from abc import ABC, abstractmethod
from decimal import Decimal

class Student(ABC):
    """This student represents a student object"""

    @abstractmethod
    def get_grade_point_average(self) -> Decimal:
        """ Return the students grade average

            Returns:
             Decimal: The student's grade point average
        """
        pass