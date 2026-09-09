import unittest

from course.course import Course
from course.department import Department


class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def test_name_is_blank_string(self) -> None:
        # Arrange
        course_name = ""
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        # Act
        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "name cannot be an empty string"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_has_only_whitespace_characters(self) -> None:
        # Arrange
        course_name = "                     "
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        # Act
        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "name cannot be an empty string"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_credit_hours_zero(self) -> None:
        """ docstring explain test function """
        # Arrange
        course_name ="intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 0

        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "credit_hours must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_credit_hours_less_than_zero(self) -> None:
        # Arrange
        course_name ="intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = -90

        with self.assertRaises(ValueError) as context:
            course = Course(course_name, department, credit_hours)

        # Assert
        expected = "credit_hours must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_new_instance(self) -> None:
        # Arrange
        course_name = "intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        # Act
        course = Course(course_name, department, credit_hours)

        # Assert (uses name mangling to obtain private attribute)
        self.assertNoLogs("intermediate software development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(90, course._Course__credit_hours)

class TestNameProperty(unittest.TestCase):
    """Defines tests for the name property."""

    def test_returns_current_state(self) -> None:
        # Arrange
        course_name ="intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        course = Course(course_name, department, credit_hours)

        # Act
        actual = course.name

        # Assert
        expected = course_name
        self.assertEqual(expected, actual)

class TestDepartmentProperty(unittest.TestCase):
    """Defines tests for the department property."""

    def test_returns_current_state(self) -> None:
        # Arrange
        course_name = "intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        self.course = Course(course_name, department, credit_hours)

        # Act
        actual = self.course.department

        # Assert
        expected = Department.COMPUTER_SCIENCE
        self.assertEqual(expected, actual)

class TestCreditHoursProperty(unittest.TestCase):
    """Defines tests for the credit_hours property."""

    def setUp(self) -> None:
        """This method is invoked to prepare the test fixture.
        This method is invoked before invoking a test method.
        """

        course_name = "intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        self.course = Course(course_name, department, credit_hours)

    def test_set_to_zero(self) -> None:
        # Act
        with self.assertRaises(ValueError) as context:
            self.course.credit_hours = 0

        # Assert
        expected = "credit_hours must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_set_to_less_than_zero(self) -> None:
        # Act
        with self.assertRaises(ValueError) as context:
            self.course.credit_hours = -90

        # Assert
        expected = "credit_hours must be a value greater than zero"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_state_modified(self) -> None:
        # Arrange
        credit_hours = 80

        # Act
        self.course.credit_hours = credit_hours

        # Assert
        expected = credit_hours
        actual = self.course._Course__credit_hours
        self.assertEqual(expected, actual)

    def test_returns_current_state(self) -> None:
        # Act
        actual = self.course.credit_hours

        # Assert
        expected = 90
        self.assertEqual(expected, actual)

class TestStr(unittest.TestCase):
    """Defines tests for the __str__ method."""

    def test_returns_string_representation(self) -> None:
        # Arrange
        course_name ="intermediate software development"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 90

        course = Course(course_name, department, credit_hours)

        # Act
        actual = course.__str__()

        # Assert
        expected = ("Course: Intermediate Software Development\n"
                    "Department: Computer Science\n"
                    "Credit Hours: 90")
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()