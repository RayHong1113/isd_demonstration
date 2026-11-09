""""Defines the StudentWindow class."""
from PySide6.QtCore import Slot
from student.college_student import CollegeStudent

from ui.base.main_window import MainWindow
from ui.student_grade_dialog import StudentGradeDialog
from decimal import Decimal




__author__ = "ACE Faculty"
__version__ = "1.0.0"

class StudentWindow(MainWindow):
    """Represents a window for selecting a student."""

    def __init__(self) -> None:
        """Initializes a new instance of the StudentWindow class."""

        super().__init__()

        self.setWindowTitle("Student Manager")
        self.__current_index = 0 
        self.__students = self.__load_student_data()
        self.__initialize_widgets()

    def __initialize_widgets(self) -> None:
        """Init the widgets in the window"""
        
        # handle navigation buttons
        self._first_button.clicked.connect(self.__on_first_button_clicked)
        self._previous_button.clicked.connect(self.__on_previous_button_clicked)
        self._next_button.clicked.connect(self.__on_next_button_clicked)
        self._last_button.clicked.connect(self.__on_last_button_clicked)

        # edit button
        self._edit_button.clicked.connect(self.__on_edit_button_clicked)

        self.__update_user_interface()

        

    def __update_user_interface(self) -> None:
        """Updates the displayed student information."""

        student = self.__students[self.__current_index]

        
        self._student_number_label.setText(str(student.student_number))
        self._name_label.setText(student.name)

        self._grade_label.setText(str(student.get_grade_point_average()))
        self._item_count_label.setText(f"{self.__current_index + 1} of " 
                                                f"{len(self.__students)}")

    @Slot()
    def __on_edit_button_clicked(self) -> None:
        """Handles the event for edit button"""
        dialog = StudentGradeDialog(self.__students[self.__current_index])

        dialog.grade_updated.connect(self.__on_grade_updated)
        dialog.exec() # opens the dialog


    def __on_grade_updated(self, grade: Decimal)-> None:
        """
            Handle the grade_updated event of the dialog window

            args:
                grade( Decimal) : the updated grade

        """
        student = self.__students[self.__current_index]
        student.set_grade_point_average(grade)
        self.__update_user_interface()

    @Slot()
    def __on_first_button_clicked(self) -> None:
        """Handles the clicked event of the first button."""

        self.__current_index = 0

        self.__update_user_interface()

    @Slot()
    def __on_previous_button_clicked(self) -> None:
        """Handles the clicked event of the previous button."""

        if self.__current_index != 0:
            self.__current_index -= 1

            self.__update_user_interface()

    @Slot()
    def __on_next_button_clicked(self) -> None:
        """Handles the clicked event of the next button."""

        if self.__current_index != len(self.__students) - 1:
            self.__current_index += 1

            self.__update_user_interface()

    @Slot()
    def __on_last_button_clicked(self) -> None:
        """Handles the clicked event of the last button."""

        self.__current_index = len(self.__students) - 1

        self.__update_user_interface()

    #endregion

    def __load_student_data(self) -> list[CollegeStudent]:
        """Loads student data.
        
        Returns:
            list[CollegeStudent]: A list of students.
        """

        students = []

        students.append(CollegeStudent("John Brunelle", Decimal('1.49')))
        students.append(CollegeStudent("Elizabeth Sinclair", Decimal('.94')))
        students.append(CollegeStudent("Angela Brock", Decimal('2.61')))
        students.append(CollegeStudent("Robert Flammand", Decimal('2.51')))
        students.append(CollegeStudent("Arthur Armstrong", Decimal('2.58')))
        students.append(CollegeStudent("Chris Mullin", Decimal('3.52')))
        students.append(CollegeStudent("Jackie Blanchard", Decimal('2.6')))
        students.append(CollegeStudent("George Shanahan", Decimal('3.0')))
        students.append(CollegeStudent("Linda Eck", Decimal('3.82')))
        students.append(CollegeStudent("Judy Gardener", Decimal('4.02')))
        students.append(CollegeStudent("Donna Smith", Decimal('4.14')))
        students.append(CollegeStudent("Eric Best", Decimal('1.38')))

        return students
