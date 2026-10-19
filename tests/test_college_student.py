"""The module defines tests for the CollegeStudent class.

Example:
    $ python -m unittest tests/test_college_student.py
"""

import unittest
from decimal import Decimal

from student.college_student import CollegeStudent

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.student_number = 9999
        self.name = "Deron Warkentin"
        self.grade_point_average = Decimal('3.2')

    def test_student_number_less_than_four_digits(self) -> None:
        # Arrange
        self.student_number = 999

        # Act
        with self.assertRaises(ValueError) as context:
            CollegeStudent(self.student_number, self.name, self.grade_point_average)

        # Assert
        self.assertEqual("student_number must be four digits greater than zero",
                         str(context.exception))
    
    def test_student_number_less_than_zero(self) -> None:
        # Arrange
        self.student_number = -999

        # Act
        with self.assertRaises(ValueError) as context:
            CollegeStudent(self.student_number, self.name, self.grade_point_average)

        # Assert
        self.assertEqual("student_number must be four digits greater than zero",
                         str(context.exception))
        
    def test_name_is_an_empty_string(self) -> None:
        # Arrange
        self.name = ""

        # Act
        with self.assertRaises(ValueError) as context:
            CollegeStudent(self.student_number, self.name, self.grade_point_average)

        # Assert
        self.assertEqual("name cannot be an empty string",
                         str(context.exception))
        
    def test_name_only_whitespace_characters(self) -> None:
        # Arrange
        self.name = "     "

        # Act
        with self.assertRaises(ValueError) as context:
            CollegeStudent(self.student_number, self.name, self.grade_point_average)

        # Assert
        self.assertEqual("name cannot be an empty string",
                         str(context.exception))
        
    def test_grade_point_average_below_range(self) -> None:
        # Arrange
        self.grade_point_average = Decimal('-3.2')

        # Act
        with self.assertRaises(ValueError) as context:
            CollegeStudent(self.student_number, self.name, self.grade_point_average)
        
        # Assert
        self.assertEqual("grade_point_average must be a Decimal "
                         "value between 0 and 4.5 (inclusive)",
                         str(context.exception))
        
    def test_grade_point_average_above_range(self) -> None:
        # Arrange
        self.grade_point_average = Decimal('4.6')

        # Act
        with self.assertRaises(ValueError) as context:
            CollegeStudent(self.student_number, self.name, self.grade_point_average)

        # Assert
        self.assertEqual("grade_point_average must be a Decimal "
                         "value between 0 and 4.5 (inclusive)",
                         str(context.exception))
        
    def test_grade_point_average_is_low_range(self) -> None:
        # Arrange
        self.grade_point_average = Decimal('0')

        # Act
        student = CollegeStudent(self.student_number, 
                                 self.name, 
                                 self.grade_point_average)

        # Assert
        self.assertEqual(self.grade_point_average,
                         student._CollegeStudent__grade_point_average)
        
    def test_grade_point_average_is_high_range(self) -> None:
        # Arrange
        self.grade_point_average = Decimal('4.5')

        # Act
        student = CollegeStudent(self.student_number, 
                                 self.name, 
                                 self.grade_point_average)

        # Assert
        self.assertEqual(self.grade_point_average,
                         student._CollegeStudent__grade_point_average)
        
    def test_initialize_new_instance(self) -> None:
        # Act
        student = CollegeStudent(self.student_number, 
                                 self.name, 
                                 self.grade_point_average)

        # Assert
        self.assertEqual(self.name, student._CollegeStudent__name)
        self.assertEqual(self.grade_point_average,
                         student._CollegeStudent__grade_point_average)

class TestStudentNumberProperty(unittest.TestCase):
    """Defines tests for the student_number property."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.student = CollegeStudent(9999, "Deron Warkentin", Decimal('3.2'))

    def test_returns_current_state(self) -> None:
        self.assertEqual(9999, self.student.student_number)

class TestNameProperty(unittest.TestCase):
    """Defines tests for the name property."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.student = CollegeStudent(9999, "Deron Warkentin", Decimal('3.2'))

    def test_returns_current_state(self) -> None:
        self.assertEqual("Deron Warkentin", self.student.name)

class TestGetGradePointAverage(unittest.TestCase):
    """Defines tests for the get_grade_point_average() method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.student = CollegeStudent(9999, "Deron Warkentin", Decimal('3.2'))

    def test_returns_current_state(self) -> None:
        self.assertEqual(Decimal('3.2'), self.student.get_grade_point_average())

class TestSetGradePointAverage(unittest.TestCase):
    """Defines tests for the set_grade_point_average() method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.student = CollegeStudent("Deron Warkentin", Decimal('3.2'))

    def test_updates_current_state(self) -> None:
        self.student.set_grade_point_average(Decimal('2.2'))

        self.assertEqual(Decimal('2.2'), self.student._CollegeStudent__grade_point_average)


class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        """Runs before each test."""

        self.student = CollegeStudent(9999, "Deron Warkentin", Decimal('3.2'))

    def test_returns_current_state(self) -> None:
        self.assertEqual("Deron Warkentin (9999)", self.student.__str__())
