import sys
import app
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize the window properties
        self.resize(800, 600)
        self.setWindowTitle("Stock Sentiment Bot")
        self.setWindowIcon(QIcon("icons/stock_sentiment_bot_icon.jpg"))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # add logo to top
        logo_label = QLabel()
        logo_pixmap = QPixmap("icons/stock_sentiment_bot_icon.jpg")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        # text input for stock ticker
        self.ticker_input = QLineEdit()
        self.ticker_input.setPlaceholderText("Enter stock ticker...")
        layout.addWidget(self.ticker_input)

        # text input for from date
        self.from_date_input = QLineEdit()
        self.from_date_input.setPlaceholderText("From...")
        layout.addWidget(self.from_date_input)

        # text input for to date
        self.to_date_input = QLineEdit()
        self.to_date_input.setPlaceholderText("To...")
        layout.addWidget(self.to_date_input)

        # submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.handle_submit)
        layout.addWidget(submit_button)

        central_widget.setLayout(layout)

    def handle_submit(self):
        input1 = self.ticker_input.text()
        input2 = self.from_date_input.text()
        input3 = self.to_date_input.text()

        print(f"Input 1: {input1}")
        print(f"Input 2: {input2}")
        print(f"Input 3: {input3}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # set up stylesheets
    with open("styles.qss", "r") as styles:
        app.setStyleSheet(styles.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())