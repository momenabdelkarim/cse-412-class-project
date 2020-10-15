"""
This file lays out the list view of any multimedia supported by the application
This includes podcasts, albums, episodes, songs, and specials
"""
from typing import Optional

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QStyle

from ui.helper_functions import icon_with_color
from ui.image_requester import ImageRequester


class MediaView(QWidget):
    def __init__(self, parent: QWidget, title_text: str, subtitle_text: str, image_url: Optional[str] = None, display_add: Optional[bool] = False):
        super().__init__(parent)

        self.__display_add = display_add
        self.setObjectName('media-view')
        self.__layout_manager = QVBoxLayout(self)
        self.__title = QLabel(title_text, self)
        self.__subtitle = QLabel(subtitle_text, self)
        self.__add_btn = QPushButton()
        self.setMaximumHeight(200)

        self.__photo = QLabel("", self)
        img_req = ImageRequester(self, self.__photo, image_url)
        img_req.request()

        self.__layout_ui()

    def __layout_ui(self):
        self.__title.setObjectName("media-title")
        self.__subtitle.setObjectName("media-subtitle")

        container = QFrame(self)
        container.setFrameShadow(QFrame.Raised)

        container.setObjectName("media-view")
        container_manager = QHBoxLayout(container)

        if self.__display_add:
            # Load icon from svg
            add_icon = icon_with_color("img/plus.svg", QColor(29, 185, 84))
            self.__add_btn.setIcon(add_icon)
            self.__add_btn.setIconSize(QSize(35, 35))
            self.__add_btn.setObjectName("add-btn")
            self.__add_btn.setFixedWidth(45)
            self.__add_btn.setFlat(True)
            container_manager.addWidget(self.__add_btn, Qt.AlignVCenter)

        # Layout title and subtitle vertically
        title_layout_manager = QVBoxLayout()
        title_layout_manager.addStretch()
        title_layout_manager.addWidget(self.__title)
        title_layout_manager.addSpacing(15)
        title_layout_manager.addWidget(self.__subtitle)
        title_layout_manager.addStretch()

        # Layout photo to the left of title stack
        container_manager.addWidget(self.__photo, Qt.AlignHCenter)
        container_manager.addSpacing(20)
        container_manager.addLayout(title_layout_manager, Qt.AlignVCenter)
        container_manager.addStretch()

        self.__layout_manager.addWidget(container)
