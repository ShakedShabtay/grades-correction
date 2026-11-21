import os
import sys
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QSpinBox,
    QTableWidget, QTableWidgetItem, QFileDialog,
    QVBoxLayout, QHBoxLayout, QHeaderView
)
from About import About


class GradesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''


        self.header_line = ''
        self.about_window = None
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Grades Correction System")
        self.resize(560, 620)




















        if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = GradesWindow()
    window.show()
    app.exec()