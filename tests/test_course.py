import unittest

from course.course import Course
from course.department import Department
from course.lecture_course import LectureCourse
from course.student import Student


class TestInit(unittest.TestCase):
    """Defines test for the constructor __init__ method."""
    def test_lecture_hall_is_empty_string(self)-> None:

        #Arrange/Act
        with self.assertRaises(ValueError) as context:
            course = LectureCourse("ISD", Department.COMPUTER_SCIENCE,90,"")

        #Assert
        self.assertEqual("lecture_hall cannot be an empty string", str(context.exception))

class TestLectureHallProperty(unittest.TestCase):
    """Defines tests for the lecture hall property"""

    def test_returns_current_state(self)-> None:
        # arrange 
        course = LectureCourse("ISD", Department.COMPUTER_SCIENCE, 90, "A202")

        # act/ assert
        self.assertEqual("A202", course.lecture_hall)

class TestEnrollStudent(unittest.TestCase):
    """Defines test for the enroll student method"""

    def setUp(self)-> None:
        # arrange
        self.course = LectureCourse("ISD", Department.COMPUTER_SCIENCE,90,"A202")

    def test_enroll_student_at_capacity(self) -> None:
        # arrange 
        capacity = Course.ENROLLMENT_LIMIT + int(Course.ENROLLMENT_LIMIT * .1)

        for _ in range(capacity):
            # name mangling prevents accidental access to backing attributes, it also bypasses the calling encapsulated method students reader ;)
            self.course._Course__students.append(Student()) # name mangling idea to make if more difficult to gain access to private member backing attributes. 
            # self.course.students.append(Student()) # accessing the read directly.

        with self.assertRaises(ValueError) as context:
            self.course.enroll_student(Student())

        self.assertEqual("Cannot enroll student; course at capacity",
                        str(context.exception))


    # def test_enroll_student_below_enrollment_limit(self) -> None:
    #     # Arrange 
        # student = Student()

        # # act
        # self.course.enroll_student(student)

        # # assert 
        # # list contains the student
        # # self.assertIn(student, self.course._Course__students)

        # self.assertEqual(3, len(self.course._Course__students))

if __name__ == "__main__":
    unittest.main()