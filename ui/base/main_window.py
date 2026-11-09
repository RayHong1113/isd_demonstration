"""Defines the MainWindow class."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, 
                               QWidget,
                               QLayout,
                               QVBoxLayout, 
                               QHBoxLayout,
                               QFormLayout,
                               QGroupBox,
                               QLabel,
                               QPushButton)

__author__ = "ACE Faculty"
__version__ = "1.0.0"

class MainWindow(QMainWindow):
    """Represents the main window of the application."""    

    def __init__(self):
        """Initializes a new instance of the MainWindow class."""

        super().__init__()

        # Main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.__initialize_widgets(layout)

        layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.adjustSize()
        self.setFixedSize(self.size())

    def __initialize_widgets(self, layout: QVBoxLayout) -> None:
        """Initializes the widgets on the window.
        
        Args:
            layout (QVBoxLayout): The layout of the window.
        """

        layout.addWidget(self.__initialize_student_groupbox())
        layout.addStretch()
        
        self._item_count_label = QLabel("99 of 99")

        layout.addWidget(self._item_count_label, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.__initialize_button_container())        

    def __initialize_student_groupbox(self) -> QGroupBox:
        """Initializes the student groupbox and containing widgets.
        
        Returns:
            QGroupBox: The student groupbox and containing widgets.
        """

        groupbox = QGroupBox("Student")
        
        layout = QFormLayout(groupbox)

        layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        student_number_label = QLabel("000000000")
        name_label = QLabel("XXXXXXXX XXXXXXXXX")
        grade_label = QLabel("0.00")

        layout.addRow("ID:", student_number_label)
        layout.addRow("Name:", name_label)
        layout.addRow("GPA:", grade_label)

        self._student_number_label = student_number_label
        self._name_label = name_label
        self._grade_label = grade_label
        
        return groupbox
    
    def __initialize_button_container(self) -> QWidget:
        """Initializes a widget containing the buttons on window.
        
        Returns:
            QWidget: A widget containing the buttons on window.
        """

        container = QWidget()

        layout = QHBoxLayout(container)

        first_button = QPushButton("<<")
        previous_button = QPushButton("<")
        edit_button = QPushButton("Edit Grade")
        next_button = QPushButton(">")
        last_button = QPushButton(">>")

        layout.addWidget(first_button)
        layout.addWidget(previous_button)
        layout.addWidget(edit_button)
        layout.addWidget(next_button)
        layout.addWidget(last_button)

        self._first_button = first_button
        self._previous_button = previous_button
        self._edit_button = edit_button
        self._next_button = next_button
        self._last_button = last_button

        return container        
