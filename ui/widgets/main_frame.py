"""
Defines the application's main view
"""
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFrame, QTabWidget, QVBoxLayout

from backend.handlers import get_all_user_playlists, cursor, get_all_media, get_all_media_objects_for_playlist
from ui.image_cache import image_cache
from ui.widgets.media_list import AddMediaListView
from ui.widgets.playlist_view import PlaylistView


class MainFrame(QFrame):

    def __init__(self, parent: QObject):
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

    def ____update_media_list_view(self):
        """
        Pulls media list data from DB
        """
        all_media = get_all_media(cursor)

        self.__add_media_view.model().update_item(all_media)


class AbstractMediaTab(QFrame):
    """
    Abstract Class to define shared functionality between the AllMedia and Playlist tabs in the
    main frame.

    DO NOT INSTANTIATE
    """

    def __init__(self, parent: QObject):
        super().__init__(parent)
        self._add_media_view = None

    def _update_media_list_view(self):
        """
        Pulls media list data from DB
        """
        all_media = get_all_media(cursor)

        self._add_media_view.model().update_item(all_media)


class PlaylistTab(AbstractMediaTab):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self.__playlist_view = PlaylistView(self, image_cache)
        self._add_media_view = AddMediaListView(self, image_cache)

        self.__layout_ui()
        self.__update_playlist_view()

        # Connect signals to slots
        self.__playlist_view.should_display_playlist.connect(self._update_media_list_view)

    def __layout_ui(self):
        self.__layout_manager.addWidget(self.__playlist_view)

        # Add dividing line
        line = QFrame(self)
        line.setObjectName("line")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.__layout_manager.addWidget(line)

        self.__layout_manager.addWidget(self._add_media_view, 1)
        self.__layout_manager.addStretch()

    def __update_playlist_view(self):
        """
        Pulls playlist data from database and updates UI to reflect the state of the DB
        """

        # Request list of playlists from the database
        current_playlists = get_all_user_playlists(cursor)

        self.__playlist_view.model().update_playlist(current_playlists)

    # Slots
    @QtCore.pyqtSlot(int)
    def _update_media_list_view(self, playlist_id: int):
        """
        Slot connected to a PlaylistView's should_display_playlist signal

        Retrieves media objects in a playlist and displays them in addMediaView
        """
        super()._update_media_list_view()

        media_list = get_all_media_objects_for_playlist(cursor, playlist_id)
        self._add_media_view.model().update_item(media_list)

class AddMediaTab(AbstractMediaTab):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self._add_media_view = AddMediaListView(self, image_cache)

        self.__layout_ui()

    def __layout_ui(self):
        self.__layout_manager.addWidget(self._add_media_view)

        self._update_media_list_view()
