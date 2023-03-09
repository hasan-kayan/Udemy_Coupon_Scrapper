import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox, QLabel, \
    QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, QComboBox
import subprocess
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt, QSize

class WebScraper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Web Scraper')
        self.setFixedSize(QSize(600, 400)) # set a fixed size for the window
        self.setStyleSheet("background-color: #143C64; color: white;") # set the background color and text color

        # Main widget
        widget = QWidget()
        self.setCentralWidget(widget)

        # Main layout
        main_layout = QVBoxLayout()
        widget.setLayout(main_layout)

        # Checkboxes
        checkboxes_layout = QHBoxLayout()
        main_layout.addLayout(checkboxes_layout)

        checkbox1 = QCheckBox('real.discount.com')
        checkboxes_layout.addWidget(checkbox1)

        checkbox2 = QCheckBox('discudemy.com')
        checkboxes_layout.addWidget(checkbox2)

        checkbox3 = QCheckBox('cuponscorpion.com')
        checkboxes_layout.addWidget(checkbox3)

        # Max Amount spinbox
        max_amount_layout = QHBoxLayout()
        main_layout.addLayout(max_amount_layout)

        max_amount_label = QLabel('Max Amount')
        max_amount_layout.addWidget(max_amount_label)

        max_amount_spinbox = QSpinBox()
        max_amount_spinbox.setMinimum(0)
        max_amount_layout.addWidget(max_amount_spinbox)

        # Course Date combobox
        course_date_layout = QHBoxLayout()
        main_layout.addLayout(course_date_layout)

        course_date_label = QLabel('Course Date')
        course_date_layout.addWidget(course_date_label)

        course_date_combobox = QComboBox()
        course_date_combobox.addItems(['2021', '2022', '2023'])
        course_date_layout.addWidget(course_date_combobox)

        # Retries combobox
        retries_layout = QHBoxLayout()
        main_layout.addLayout(retries_layout)

        retries_label = QLabel('Retries')
        retries_layout.addWidget(retries_label)

        retries_combobox = QComboBox()
        retries_combobox.addItems(['0', '1', '2', '3'])
        retries_layout.addWidget(retries_combobox)

        # Scrape button
        scrape_button_layout = QHBoxLayout()
        main_layout.addLayout(scrape_button_layout)

        scrape_button = QPushButton('Scrape')
        scrape_button_layout.addWidget(scrape_button)

        # Connect button click to function
        scrape_button.clicked.connect(self.start_scraping)

        # Set the window to fill the screen
        screen = QApplication.instance().primaryScreen()
        size = screen.size()
        self.setGeometry(0, 0, size.width(), size.height())

    def start_scraping(self):
        try:
            subprocess.call(['python', 'scrapy.py'])
        except subprocess.CalledProcessError as e:
            print("Error: ", e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebScraper()
    window.showFullScreen() # set the window to show in full-screen mode
    sys.exit(app.exec_())
