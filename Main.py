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

        self.title_label = QLabel("Student Grades Manager")
        self.title_label.setObjectName("title")

    
        self.load_btn = QPushButton("Load Grades File")
        self.load_btn.clicked.connect(self.load_file)

        self.file_label = QLabel("No file selected")

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.load_btn)
        top_layout.addWidget(self.file_label)
        top_layout.addStretch()

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.bonus_label = QLabel("Bonus Points (Press ENTER):")
        self.bonus_input = QSpinBox()
        self.bonus_input.setRange(-100, 100)
        self.bonus_input.lineEdit().returnPressed.connect(self.apply_bonus)

        bonus_layout = QHBoxLayout()
        bonus_layout.addWidget(self.bonus_label)
        bonus_layout.addWidget(self.bonus_input)
        bonus_layout.addStretch()

        self.update_btn = QPushButton("Update File")
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update_file)

        self.about_btn = QPushButton("About")
        self.about_btn.setObjectName("about_btn")
        self.about_btn.clicked.connect(self.open_about)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.update_btn)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.about_btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.table)
        main_layout.addLayout(bonus_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

















        if __name__ == "__main__":
    app = QApplication()

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = GradesWindow()
    window.show()
    app.exec()