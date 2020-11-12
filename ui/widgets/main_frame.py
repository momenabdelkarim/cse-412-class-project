"""
Defines the application's main view
"""
from typing import Optional

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFrame, QTabWidget, QVBoxLayout

from ui.image_cache import ImageCache
from ui.widgets.media_list import AddMediaListView
from ui.widgets.playlist_view import PlaylistView

image_cache: Optional[ImageCache] = None


class MainFrame(QFrame):

    def __init__(self, parent: QObject):
        global image_cache
        image_cache = ImageCache(parent)

        super().__init__(parent)

        self.__tabs = QTabWidget(self)
        self.__playlist_tab = PlaylistTab(self)
        self.__add_media_tab = AddMediaTab(self)
        self.__layout_manager = QVBoxLayout(self)

        self.__layout_ui()

    def __layout_ui(self):
        # Set up tabs
        self.__tabs.addTab(self.__playlist_tab, "My Playlists")
        self.__tabs.addTab(self.__add_media_tab, "All Media")

        self.__layout_manager.addWidget(self.__tabs)


class PlaylistTab(QFrame):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self.__playlist_view = PlaylistView(self, image_cache)
        self.__add_media_view = AddMediaListView(self, image_cache)

        self.__layout_ui()

    def __layout_ui(self):
        self.__layout_manager.addWidget(self.__playlist_view)

        # Add dividing line
        line = QFrame(self)
        line.setObjectName("line")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.__layout_manager.addWidget(line)

        self.__layout_manager.addWidget(self.__add_media_view, 1)
        self.__layout_manager.addStretch()


class AddMediaTab(QFrame):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self.__add_media_view = AddMediaListView(self, image_cache)

        self.__layout_ui()

    def __layout_ui(self):
        self.__layout_manager.addWidget(self.__add_media_view)
