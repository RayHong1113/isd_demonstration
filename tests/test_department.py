import unittest

from course.department import Department

__author__ = "ACE Faculty mbialowas@rrc.ca"
__version__ = "1.0.0"

class TestDepartment(unittest.TestCase):

    def test_enumeration_values_initialized(self):

        # Arrange, Act, Assert

        self.assertEqual(1, Department.COMPUTER_SCIENCE.value)
        self.assertEqual(2, Department.EDUCATION.value)
        self.assertEqual(3, Department.ENGINEERING.value)
        self.assertEqual(4, Department.MEDICINE.value)


if __name__ == "__main__":
    unittest.main()