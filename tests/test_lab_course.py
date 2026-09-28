"""The module defines tests for the LabCourse class.

Example:
    $ python -m unittest tests/test_course.py
"""

import unittest

from course.department import Department
from course.course import Course
from course.lab_course import LabCourse
from course.student import Student

__author__ = "ACE Faculty <mbialowas@rrc.ca>"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def test_initialize_new_instance(self) -> None:
        # Arrange/Act
        course = LabCourse("Intermediate Software Development", 
                           Department.COMPUTER_SCIENCE, 
                           90)

        # Assert
        self.assertEqual("Intermediate Software Development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(90, course._Course__credit_hours)
        self.assertEqual([], course._Course__students)
        self.assertEqual([], course._LabCourse__lab_equipment)

class TestEnrollStudent(unittest.TestCase):
    """Defines tests for the enroll_student method."""

    def setUp(self) -> None:
        # Arrange
        self.course = LabCourse("Intermediate Software Development", 
                                Department.COMPUTER_SCIENCE, 
                                90)

    def test_enroll_student_at_capacity(self) -> None:
        for _ in range(int(Course.ENROLLMENT_LIMIT / 2)):
            self.course._Course__students.append(Student())

        # Act
        with self.assertRaises(ValueError) as context:
            self.course.enroll_student(Student())

        # Assert
        self.assertEqual("Cannot enroll student, course at capacity",
                         str(context.exception))
        
    def test_enroll_student_below_capacity(self) -> None:
        # Arrange
        student = Student()
        
        # Act
        self.course.enroll_student(student)

        # Assert
        # List contains the student
        self.assertIn(student, self.course._Course__students)

        # List contains the correct number of students
        self.assertEqual(1, len(self.course._Course__students))

class TestAddLabEquipment(unittest.TestCase):
    """Defines tests for the add_lab_equipment method."""

    def setUp(self) -> None:
        # Arrange
        self.course = LabCourse("Intermediate Software Development", 
                                Department.COMPUTER_SCIENCE, 
                                90)

    def test_equipment_is_empty_string(self) -> None:
        # Act
        with self.assertRaises(ValueError) as context: 
            self.course.add_lab_equipment("")

        # Assert
        self.assertEqual("equipment cannot be empty",
                         str(context.exception))
        
    def test_equipment_already_added(self) -> None:
        # Arrange
        lab_equipment = ["Microscope"]
        self.course._LabCourse__lab_equipment = lab_equipment
        
        # Act
        self.course.add_lab_equipment("microscope")

        # Assert
        self.assertCountEqual(lab_equipment, self.course._LabCourse__lab_equipment)

    def test_equipment_is_updated(self) -> None:
        # Arrange
        lab_equipment = "microscope"

        # Act
        self.course.add_lab_equipment(lab_equipment)

        # Assert
        self.assertIn(lab_equipment.title(), self.course._LabCourse__lab_equipment)
        self.assertEqual(1, len(self.course._LabCourse__lab_equipment))

class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        # Arrange
        self.course = LabCourse("Intermediate Software Development", 
                                Department.COMPUTER_SCIENCE, 
                                90)
        self.course._LabCourse__lab_equipment = ["Microscope"]

    def test_returns_string_representation(self) -> None:
        # Act
        actual = self.course.__str__()

        # Assert
        expected = ("Course: Intermediate Software Development\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90\n"
                    "Lab Equipment: ['Microscope']")
        self.assertEqual(expected, actual)

