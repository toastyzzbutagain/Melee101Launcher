# Import Modules:
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap

# Main Function / App Objects & Settings:
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("MeleeLauncher")
main_window.setGeometry(100, 100, 400, 300)
main_window.resize(500, 500)

# Create App Object:
self_font = QFont("Trebuchet MS", 12)
title_font = QFont("Noto Sans", 45, QFont.Bold)
app.setFont(self_font)
title = QLabel("MeleeLauncher")
title.setFont(title_font)
title.setStyleSheet("color: #FF0000;")  # Set title color to red

text1 = QLabel("Welcome to MeleeLauncher! This is a simple launcher for Melee101.")
text2 = QLabel("Click the \"Launch\" button to do what it says.")

launch_button = QPushButton("Launch")
help_button = QPushButton("Help")
exit_button = QPushButton("Exit")

# All Design:
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
#
row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)

row3.addWidget(launch_button)
row3.addWidget(help_button)
row3.addWidget(exit_button)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)



main_window.setLayout(master_layout)



# Events:

# Run App:
main_window.show()
app.exec_()