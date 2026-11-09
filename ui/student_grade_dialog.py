"""Defines the StudentGradeDialog class."""

from student.college_student import CollegeStudent

from ui.base.grade_dialog import GradeDialog

__author__ = "ACE Faculty"
__version__ = "1.0.0"

class StudentGradeDialog(GradeDialog):
    """Represents a dialog window for updating a student's grade point
    average.
    """

    def __init__(self, student: CollegeStudent) -> None:
        """Initializes a new instance of the StudentGradeDialog class.
        
        Args:
            student (CollegeStudent): The student whose grade is being
                updated.
        """

        super().__init__()
