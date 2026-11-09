"""Defines the GradeDialog class."""

from __future__ import annotations
from decimal import Decimal

from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import (QApplication,
                               QDialog,
                               QVBoxLayout,
                               QGridLayout,
                               QFormLayout,
                               QWidget,
                               QGroupBox,
                               QLabel, 
                               QLineEdit, 
                               QPushButton, 
                               QComboBox,
                               QCheckBox,
                               QSizePolicy)

__author__ = "ACE Faculty"
__version__ = "1.0.0"

class GradeDialog(QDialog):
    """Represents a dialog window used for determining an student's 
    grade.
    """

    GRADES = {
        "A+": Decimal('4.5'),
        "A": Decimal('4'),
        "B+": Decimal('3.5'),
        "B": Decimal('3'),
        "C+": Decimal('2.5'),
        "C": Decimal('2'),
        "D": Decimal('1'),
        "F": Decimal('0')
    }
    """The letter grades with associated grade point average."""

    def __init__(self):
        """Initializes a new instance of the GradeDialog class."""

        super().__init__()

        self.setFixedSize(300, 460)

        layout = QVBoxLayout(self)

        self.__initialize_widgets(layout)

    def __initialize_widgets(self, layout: QVBoxLayout) -> None:
        """Initializes the widgets on the window.
        
        Args:
            layout (QVBoxLayout): The main layout of the window."""

        layout.addWidget(self.__initialize_student_detail_groupbox())
        layout.addWidget(self.__initialize_grade_entry_groupbox())
        layout.addWidget(self.__initialize_extra_curricular_groupbox())

        widget = QWidget()
        widget_layout = QVBoxLayout(widget)
        widget_layout.addWidget(QLabel("GPA"))
        grade_label = QLabel("0.0")
        color = QApplication.palette().color(QPalette.ColorRole.WindowText).name()

        grade_label.setStyleSheet(f"""border: 1px solid {color}; 
                                  padding: 5px;
                                  font-size: 32px;
                                  color: {color};""")
        grade_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        grade_label.adjustSize()
        grade_label.setMinimumWidth(grade_label.width())
        widget_layout.addWidget(grade_label)
        widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)

        update_button = QPushButton("Update Grade")
        update_button.setFixedWidth(100)

        layout.addStretch()
        layout.addWidget(update_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self._grade_label = grade_label
        self._update_button = update_button

    def __initialize_student_detail_groupbox(self) -> QGroupBox:
        """Initializes the student details groupbox and widgets.
        
        Returns:
            QGroupBox: The student details groupbox and widgets.
        """

        groupbox = QGroupBox("Student Information")
        layout = QFormLayout(groupbox)        

        number_label = QLabel("00000000")
        layout.addRow(QLabel("ID:"), number_label)

        name_label = QLabel("XXXXXXXX XXXXXXXX")
        layout.addRow(QLabel("Name:"), name_label)

        self._student_name_label = name_label
        self._student_number_label = number_label

        return groupbox

    def __initialize_grade_entry_groupbox(self) -> QGroupBox:
        """Initializes the grade entry groupbox and widgets.
        
        Returns:
            QGroupBox: The grade entry groupbox and widgets.
        """

        groupbox = QGroupBox()
        layout = QGridLayout(groupbox)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.setSpacing(10)

        layout.addWidget(QLabel("Grade"), 0, 0)
        layout.addWidget(QLabel("Credit Hours"), 0, 1)

        grade_comboboxes: list[QComboBox] = \
            [QComboBox(), QComboBox(), QComboBox()]

        for index in range(len(grade_comboboxes)):
            combobox: QComboBox = grade_comboboxes[index]
            combobox.addItems(list(self.GRADES.keys()))
            combobox.setFixedWidth(60)

            layout.addWidget(combobox, index + 1, 0)

        credit_hour_line_edits: list[QLineEdit] = \
            [QLineEdit(), QLineEdit(), QLineEdit()]

        for index in range(len(credit_hour_line_edits)):
            line_edit: QLineEdit = credit_hour_line_edits[index]
            line_edit.setFixedWidth(80)

            layout.addWidget(line_edit, index + 1, 1)

        self._grade_comboboxes = grade_comboboxes
        self._credit_hour_line_edits = credit_hour_line_edits

        return groupbox

    def __initialize_extra_curricular_groupbox(self) -> QGroupBox:
        """Initializes the extra curricular groupbox and widgets.
        
        Returns:
            QGroupBox: The extra curricular groupbox and widgets.
        """

        groupbox = QGroupBox("Extra Curricular Activities")
        
        layout = QVBoxLayout(groupbox)

        self._volunteer_checkbox = QCheckBox("Volunteer")
        self._student_council_checkbox = QCheckBox("Student Council")

        layout.addWidget(self._volunteer_checkbox)
        layout.addWidget(self._student_council_checkbox)

        return groupbox
