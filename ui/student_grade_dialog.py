"""Defines the StudentGradeDialog class."""
from PySide6.QtCore import Slot
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

        self.__student = student
        self.setWindowTitle(f"Grade Edit - {student.name}")
        self.__initialize_widgets()

    def __initialize_widgets(self):
        """Initialize the widgets found on StudentGradeDialog"""
        student= self.__student

        # populate the widgets with values from student
        self._student_number_label.setText(str(student.student_number))
        self._student_name_label.setText(student.name)

        self._grade_label.setText("")
        self._update_button.setEnabled(False)

        for combobox in self._grade_comboboxes:
            combobox.setCurrentIndex(-1)

        for line_edit in self._credit_hour_line_edits:
            line_edit.setText("")


        self._volunteer_checkbox.checkStateChanged.connect(self.__on_input_changed)


    @Slot()
    def __on_input_changed(self) -> None:
        """Handles the changed events for input widgets on this window"""
        
        total_quality_points = Decimal(0)
        total_credit_hours = 0

        for combobox, line_edits in \
            zip(self._grade_comboboxes, self._credit_hour_line_edits):
                if combobox() == -1 or \
                    line_edit.text() == 0:
                    self._grade_label.setText("nil")
                    return
