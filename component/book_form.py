from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class BookForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("book_form")

        layout = QVBoxLayout(self)

        self.title = QLabel("no book choosed")
        layout.addWidget(self.title)

    def show_book(self, book):
        self.title.setText(book.title)

        self.setStyleSheet("""
            QWidget#book_form{
                background-color: lightblue;
            }
        """)