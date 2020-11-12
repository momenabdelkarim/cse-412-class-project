"""
This file defines all of the QDialog widgets used throughout the application
"""
from typing import Optional

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton

from ui.widgets.model.entities import Media


class AddToPlaylistDialog(QDialog):
    """
    Allows a user to select a playlist to save a given media object to
    """

    def __init__(self, parent: QObject, media: Media):
        super().__init__(parent)
        self.setWindowTitle(" ")

        self.__media = media
        self.__selected_playlist: Optional[int] = None
        self.__layout_manager = QVBoxLayout(self)
        self.__combo_box = QComboBox(self)
        self.__add_btn = QPushButton("Add", self)

        # Connect signals to slots
        self.__add_btn.clicked.connect(lambda: self.accept())
        self.__layout_ui()

    def __layout_ui(self):
        # Set up header label
        header_text = f"Where do you want to save {self.__media.name}?"
        header_label = QLabel(header_text, self)
        header_label.setObjectName("dialog-header")
        self.__layout_manager.addWidget(header_label)

        # TODO: Request playlists from DB
        playlists = ["Playlist 1", "Playlist 2", "Playlist 3"]
        self.__combo_box.addItems(playlists)
        self.__combo_box.setAutoFillBackground(True)
        self.__layout_manager.addWidget(self.__combo_box)

        # Add button
        self.__layout_manager.addSpacing(10)
        self.__layout_manager.addWidget(self.__add_btn, Qt.AlignCenter)

    def get_selection(self) -> int:
        """
        Returns the selection index
        """
        return self.__combo_box.currentIndex()
