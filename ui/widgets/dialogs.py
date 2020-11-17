"""
This file defines all of the QDialog widgets used throughout the application
"""
from typing import Optional

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit

from backend.handlers import cursor, get_all_user_playlists
from ui.widgets.model.entities import Media, Playlist


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

        playlists = [plist.name for plist in get_all_user_playlists(cursor)]
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


class RenamePlaylistDialog(QDialog):
    """
    This dialog allows a user to rename an existing playlist for update in the DB and in the UI
    """

    def __init__(self, parent: QObject, playlist: Playlist):
        super().__init__(parent)
        self.setWindowTitle(" ")

        self.__playlist = playlist
        self.__layout_manager = QVBoxLayout(self)
        self.__name_line_edit = QLineEdit(self)
        self.__name_line_edit.setPlaceholderText("New name")

        self.__finish_btn = QPushButton("Finish", self)

        # Connect signals to slots
        self.__finish_btn.clicked.connect(lambda: self.accept())
        self.__layout_ui()

    def __layout_ui(self):
        # Set up header label
        header_text = f"What would you like to rename {self.__playlist.name} to?"
        header_label = QLabel(header_text, self)
        header_label.setObjectName("dialog-header")
        self.__layout_manager.addWidget(header_label)

        self.__layout_manager.addWidget(self.__name_line_edit)

        # Finish button
        self.__layout_manager.addSpacing(10)
        self.__layout_manager.addWidget(self.__finish_btn, Qt.AlignCenter)

    def get_new_name(self) -> str:
        """
        Returns the selected name
        """
        return self.__name_line_edit.text()
