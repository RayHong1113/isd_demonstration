"""The module defines tests for the LectureCourse class.

Example:
    $ python -m unittest tests/test_course.py
"""

import unittest

from department.department import Department
from course.course import Course
from course.lecture_course import LectureCourse
from student.student import Student

__author__ = "ACE Faculty <mbialowas@rrc.ca>"
__version__ = "1.0.0"

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def test_lecture_hall_is_empty_string(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            course = LectureCourse("Intermediate Software Development", 
                            Department.COMPUTER_SCIENCE, 
                            90,
                            "")

        # Assert
        self.assertEqual("lecture_hall cannot be an empty string", 
                         str(context.exception))
        
    def test_lecture_hall_only_whitespace(self) -> None:
        # Arrange/Act
        with self.assertRaises(ValueError) as context:
            course = LectureCourse("Intermediate Software Development", 
                            Department.COMPUTER_SCIENCE, 
                            90,
                            "     ")

        # Assert
        self.assertEqual("lecture_hall cannot be an empty string", 
                         str(context.exception))

    def test_initialize_new_instance(self) -> None:
        # Arrange/Act
        course = LectureCourse("Intermediate Software Development", 
                           Department.COMPUTER_SCIENCE, 
                           90,
                           "W212")

        # Assert
        self.assertEqual("Intermediate Software Development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(90, course._Course__credit_hours)
        self.assertEqual([], course._Course__students)
        self.assertEqual("W212", course._LectureCourse__lecture_hall)

class TestLectureHallProperty(unittest.TestCase):
    """Defines tests for the lecture_hall property."""

    def test_returns_current_state(self) -> None:
        # Arrange
        course = LectureCourse("Intermediate Software Development", 
                           Department.COMPUTER_SCIENCE, 
                           90,
                           "W212")
        
        # Act/Assert
        self.assertEqual("W212", course.lecture_hall)

class TestEnrollStudent(unittest.TestCase):
    """Defines tests for the enroll_student method."""

    def setUp(self) -> None:
        # Arrange
        self.course = LectureCourse("Intermediate Software Development", 
                                Department.COMPUTER_SCIENCE, 
                                90,
                                "W212")

    def test_enroll_student_at_capacity(self) -> None:
        # Arrange
        capacity = Course.ENROLLMENT_LIMIT + int(Course.ENROLLMENT_LIMIT * .1)

        for _ in range(capacity):
            self.course._Course__students.append(Student())

        # Act
        with self.assertRaises(ValueError) as context:
            self.course.enroll_student(Student())

        # Assert
        self.assertEqual("Cannot enroll student; course at capacity",
                         str(context.exception))

    def test_enroll_student_at_enrollment_limit(self) -> None:
        # Arrange
        for _ in range(Course.ENROLLMENT_LIMIT):
            self.course._Course__students.append(Student())

        student = Student()

        # Act
        self.course.enroll_student(student)

        # Assert
        # List contains the student
        self.assertIn(student, self.course._Course__students)

        # List contains the correct number of students
        self.assertEqual(Course.ENROLLMENT_LIMIT + 1, len(self.course._Course__students))

    def test_enroll_student_below_enrollment_limit(self) -> None:
        # Arrange
        student = Student()
        
        # Act
        self.course.enroll_student(student)

        # Assert
        # List contains the student
        self.assertIn(student, self.course._Course__students)

        # List contains the correct number of students
        self.assertEqual(1, len(self.course._Course__students))

class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def setUp(self) -> None:
        # Arrange
        self.course = LectureCourse("Intermediate Software Development", 
                                Department.COMPUTER_SCIENCE, 
                                90,
                                "W212")

    def test_returns_string_representation(self) -> None:
        # Act
        actual = self.course.__str__()

        # Assert
        expected = ("Course: Intermediate Software Development\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90\n"
                    "Lecture Hall: W212")
        self.assertEqual(expected, actual)

