import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize

from styles.styles import APP_STYLE
from PyQt5.QtGui import QIcon
from component.book_menu import BookWin
from component.Author_menu import AuthorWin
from component.Catergory_menu import CategoryWin
from component.Designer_menu import DesignerWin
from component.Language_menu import LanguageWin
from component.Publisher_menu import PublisherWin
from component.Resource_menu import ResourceWin
from component.Translator_menu import TranslatorWin
from component.book_form import BookForm





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 500)
        self.setup_menu()
        self.setup_central_widget()
    def setup_menu(self):
        menu = self.menuBar()

        book_menu = menu.addMenu("Book")
        member_menu = menu.addMenu("Members")
        Setting_menu = menu.addMenu("Setting")
        help_menu =menu.addMenu("Help")

        book_menu.addAction(QAction("Add", self))
        book_menu.addAction(QAction("Edit", self))
        book_menu.addAction(QAction("Delete", self))
        book_menu.addAction(QAction("Search", self))

        member_menu.addAction(QAction("Add", self))
        member_menu.addAction(QAction("Edit", self))
        member_menu.addAction(QAction("Delete", self))
        member_menu.addAction(QAction("Search", self))

        Setting_menu.addAction(QAction("Theme", self))
        Setting_menu.addAction(QAction("Notification", self))

        help_menu.addAction(QAction("Setting", self))
        help_menu.addAction(QAction("FAQ", self))

        exit_action = QAction("Exit", self)
        help_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close)

    def setup_central_widget(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        left_panell = QWidget()
        left_panell.setObjectName("left_panell")
        left_panell.setFixedWidth(45)
        left_layout2 = QVBoxLayout(left_panell)
        left_layout2.setContentsMargins(0, 7, 2, 0)
        left_layout2.setSpacing(0)

        button_book = QPushButton("")
        button_book.setIcon(QIcon("img/book(w).svg"))

        button_user = QPushButton("")
        button_user.setIcon(QIcon("img/user(w).svg"))

        button_author = QPushButton("")
        button_author.setIcon(QIcon("img/pencil-alt(W).svg"))

        button_publisher = QPushButton("")
        button_publisher.setIcon(QIcon("img/newspaper(W).svg"))

        button_trans = QPushButton("")
        button_trans.setIcon(QIcon("img/earth-americas(W).svg"))

        button_language = QPushButton("")
        button_language.setIcon(QIcon("img/language(W).svg"))

        button_category = QPushButton("")
        button_category.setIcon(QIcon("img/layer-group(W).svg"))

        button_designer = QPushButton("")
        button_designer.setIcon(QIcon("img/compass-drafting(W).svg"))

        button_resources = QPushButton("")
        button_resources.setIcon(QIcon("img/file-brackets-curly(W).svg"))


        left_layout2.addWidget(button_book)
        left_layout2.addWidget(button_user)
        left_layout2.addWidget(button_author)
        left_layout2.addWidget(button_publisher)
        left_layout2.addWidget(button_trans)
        left_layout2.addWidget(button_language)
        left_layout2.addWidget(button_category)
        left_layout2.addWidget(button_designer)
        left_layout2.addWidget(button_resources)

        left_layout2.addStretch()

        left_panel = QWidget()
        left_panel.setObjectName("left_panel")
        left_panel.setFixedWidth(220)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        #
        # self.btn_authors = QPushButton("Authors")
        # self.btn_books = QPushButton("Books")
        #
        # left_layout.addWidget(self.btn_authors)
        # left_layout.addWidget(self.btn_books)

        self.book_page=BookWin()
        self.author_page=AuthorWin()
        self.category_page=CategoryWin()
        self.designer_page=DesignerWin()
        self.language_page=LanguageWin()
        self.publisher_page=PublisherWin()
        self.resource_page=ResourceWin()
        self.translator_page=TranslatorWin()

        self.left_stack=QStackedWidget()

        self.left_stack.addWidget(self.book_page)
        self.left_stack.addWidget(self.author_page)
        self.left_stack.addWidget(self.category_page)
        self.left_stack.addWidget(self.designer_page)
        self.left_stack.addWidget(self.language_page)
        self.left_stack.addWidget(self.publisher_page)
        self.left_stack.addWidget(self.resource_page)
        self.left_stack.addWidget(self.translator_page)

        left_layout.addWidget(self.left_stack)
        button_book.clicked.connect(lambda: self.left_stack.setCurrentIndex(0))
        button_author.clicked.connect(lambda: self.left_stack.setCurrentIndex(1))
        button_category.clicked.connect(lambda: self.left_stack.setCurrentIndex(2))
        button_designer.clicked.connect(lambda: self.left_stack.setCurrentIndex(3))
        button_language.clicked.connect(lambda: self.left_stack.setCurrentIndex(4))
        button_publisher.clicked.connect(lambda: self.left_stack.setCurrentIndex(5))
        button_resources.clicked.connect(lambda: self.left_stack.setCurrentIndex(6))
        button_trans.clicked.connect(lambda: self.left_stack.setCurrentIndex(7))







        left_layout.addStretch()
        self.book_form = BookForm()
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addWidget(self.book_form)
        self.book_page.bookClicked.connect(self.book_form.show_book)
        # self.stack = QStackedWidget()
        #
        # # self.author_page = AuthorPage()
        # # self.book_page = BookPage()
        # #
        # # self.stack.addWidget(self.author_page)
        # # self.stack.addWidget(self.book_page)

        # right_layout.addWidget(self.stack)

        # self.btn_authors.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        # self.btn_books.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        main_layout.addWidget(left_panell)
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

