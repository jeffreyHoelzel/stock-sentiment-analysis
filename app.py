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

        # set up general layout
        layout = QVBoxLayout()

        # # add logo to top
        # logo_label = QLabel()
        # logo_pixmap = QPixmap("icons/stock_sentiment_bot_icon.jpg")
        # logo_label.setPixmap(logo_pixmap)
        # logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # logo_label.setObjectName("logo")
        # # scale pixmap to label
        # logo_label.setScaledContents(True)
        # # set label to exact size of pixmap
        # logo_label.setFixedSize(logo_pixmap.size())
        # layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.description = QLabel()
        self.description.setText("This is a stock sentiment bot.\nEnter a stock ticker and dates to analyze the stock sentiment over that period of time.")
        self.description.setFixedSize(500, 200)
        self.description.setObjectName("description")
        layout.addWidget(self.description, alignment=Qt.AlignmentFlag.AlignCenter)

        # text input for stock ticker
        self.ticker_input = QLineEdit()
        self.ticker_input.setPlaceholderText("Enter stock ticker...")
        self.ticker_input.setObjectName("data-input")
        layout.addWidget(self.ticker_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # text input for from date
        self.from_date_input = QLineEdit()
        self.from_date_input.setPlaceholderText("From date...")
        self.from_date_input.setObjectName("data-input")
        layout.addWidget(self.from_date_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # text input for to date
        self.to_date_input = QLineEdit()
        self.to_date_input.setPlaceholderText("To date...")
        self.to_date_input.setObjectName("data-input")
        layout.addWidget(self.to_date_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setObjectName("submit-button")
        self.submit_button.clicked.connect(self.handle_submit)
        layout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignCenter)

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