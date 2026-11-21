from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class About(QWidget):
    def __init__(self, github_url="https://github.com/ShakedShabtay/grades-correction.git"):
        super().__init__()
        self.github_url = github_url
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("About")
        self.resize(360, 420)

        self.title_label = QLabel("Developer Information")
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignCenter)