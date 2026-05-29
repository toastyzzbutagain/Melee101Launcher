import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont

class MyStyledLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 1. DEFINE BUILT-IN FONTS
        # Impact gives an aggressive, clean gaming title/button look.
        # Segoe UI, Arial, or Helvetica act as the secondary clean UI fonts.
        self.title_font = "Impact"
        self.button_font = "Impact, Segoe UI, Arial, Helvetica"

        # Apply a base font globally as a fallback
        self.setFont(QFont("Segoe UI", 10))

        # 2. CONFIGURE WINDOW PROPERTIES
        if os.path.exists('my_icon.png'):
            self.setWindowIcon(QIcon('my_icon.png'))
        
        self.setWindowTitle('MeleeLauncher')
        self.setFixedSize(350, 420)

        # Main layout structure
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(30, 30, 30, 30)

        # 3. LOGO / BANNER AREA
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        
        logo_path = 'game_logo.png' 
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            scaled_pixmap = pixmap.scaled(280, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo_label.setPixmap(scaled_pixmap)
        else:
            # Elegant text-based alternative using the built-in Impact font if image is missing
            self.logo_label.setText('MELEE:101')
            self.logo_label.setStyleSheet(f"""
                font-family: '{self.title_font}'; 
                font-size: 32px; 
                color: #ffffff; 
                letter-spacing: 2px;
            """)
            
        layout.addWidget(self.logo_label)

        # 4. INTERFACE BUTTONS & STYLESHEETS
        
        # Play Button (Primary Action)
        self.play_btn = QPushButton("PLAY GAME")
        self.play_btn.setMinimumHeight(55)
        self.play_btn.setStyleSheet(f"""
            QPushButton {{
                font-family: '{self.title_font}';
                font-size: 18px; 
                font-weight: bold;
                background-color: #ff4655; 
                color: white; 
                border: none;
                border-radius: 4px;
                letter-spacing: 1px;
            }}
            QPushButton:hover {{
                background-color: #e53e4e; 
            }}
            QPushButton:pressed {{
                background-color: #cc3746; 
            }}
        """)
        self.play_btn.clicked.connect(self.launch_game)
        layout.addWidget(self.play_btn)

        # Help Button (Secondary Action)
        self.help_btn = QPushButton("HELP & CONTROLS")
        self.help_btn.setMinimumHeight(40)
        self.help_btn.setStyleSheet(f"""
            QPushButton {{
                font-family: '{self.button_font}';
                font-size: 11px;
                font-weight: bold;
                background-color: #3f4248; 
                color: #dcddde; 
                border: 1px solid #4f545c;
                border-radius: 4px;
                letter-spacing: 0.5px;
            }}
            QPushButton:hover {{
                background-color: #4f545c;
                color: white;
            }}
            QPushButton:pressed {{
                background-color: #2f3136;
            }}
        """)
        self.help_btn.clicked.connect(self.show_help)
        layout.addWidget(self.help_btn)

        # About Button (Secondary Action)
        self.about_btn = QPushButton("ABOUT THE DEVS")
        self.about_btn.setMinimumHeight(40)
        self.about_btn.setStyleSheet(f"""
            QPushButton {{
                font-family: '{self.button_font}';
                font-size: 11px;
                font-weight: bold;
                background-color: #3f4248;
                color: #dcddde;
                border: 1px solid #4f545c;
                border-radius: 4px;
                letter-spacing: 0.5px;
            }}
            QPushButton:hover {{
                background-color: #4f545c;
                color: white;
            }}
            QPushButton:pressed {{
                background-color: #2f3136;
            }}
        """)
        self.about_btn.clicked.connect(self.show_about)
        layout.addWidget(self.about_btn)

        self.setLayout(layout)

        # Global styling for main launcher background
        self.setStyleSheet("background-color: #18191c; color: white;")

    # --- Actions ---

    def launch_game(self):
        """Launches your game build."""
        game_command = [r"bin\game.exe"] 
        try:
            subprocess.Popen(game_command)
            self.showMinimized() 
        except Exception as e:
            QMessageBox.critical(self, "Launch Error", f"Could not launch game executable:\n{str(e)}")

    def show_help(self):
        help_text = (
            "<h3>Controls & Troubleshooting</h3>"
            "When you are playing the game, the tutorial will tell you how to play.<br>"
            "If the game fails to boot, verify your graphics drivers are updated."
        )
        QMessageBox.information(self, "Help Guide", help_text)

    def show_about(self):
        about_text = (
            "<h3>About This Game</h3>"
            "Developed by the same team behind Melee:101.<br><br>"
            "Built with Python and PyQt5."
        )
        QMessageBox.about(self, "About", about_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = MyStyledLauncher()
    launcher.show()
    sys.exit(app.exec_())