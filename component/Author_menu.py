import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize


from PyQt5.QtGui import QIcon
from adapters.author_data_adapter import AuthorDataAdapter
class AuthorWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("author_page")
        self.setup_ui()
    def setup_ui(self):
        self.setStyleSheet(open("styles/leftpanelstyles.qss").read())
        layout = QVBoxLayout(self)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFixedWidth(180)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setFixedHeight(self.height())
        scroll.setContentsMargins(0, 0, 0, 0)

        content = QWidget()

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        content.setObjectName("contentWidget")

        scroll.setObjectName("mainScroll")
        s=AuthorDataAdapter.get_all()


        for i in s :
            btn_add = QPushButton(i.name)
            btn_add.setObjectName("boButton")
            content_layout.addWidget(btn_add)
        content_layout.addStretch()
        scroll.setWidget(content)
        layout.addWidget(scroll)