"""This module contains the program for client services."""

import sys

from PySide6.QtWidgets import QApplication

from ui.student_window import StudentWindow

__author__ = "ACE Faculty"
__version__ = "1.0.0"

def main() -> None:
    """The main entry point to the application."""

    application = QApplication([])
    main_window = StudentWindow()

    main_window.show()
    sys.exit(application.exec())

if __name__ == "__main__":
    main()
