"""
Defines the application's main view
"""

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QFrame, QTabWidget, QVBoxLayout, QPushButton, QHBoxLayout

from backend.handlers import cursor, get_all_media, get_all_media_objects_for_playlist
from ui.helper_functions import show_child_window
from ui.image_cache import image_cache
from ui.widgets.filter_view import FilterView
from ui.widgets.media_list import AllMediaListView, GenericSubItemListView
from ui.widgets.playlist_view import PlaylistView


class MainFrame(QFrame):

    def __init__(self, parent: QObject):
        super().__init__(parent)

        self.__tabs = QTabWidget(self)
        self.__playlist_tab = PlaylistTab(self)
        self.__all_media_tab = AllMediaTab(self)
        self.__layout_manager = QVBoxLayout(self)

        self.__layout_ui()

    def __layout_ui(self):
        # Set up tabs
        self.__tabs.addTab(self.__playlist_tab, "My Playlists")
        self.__tabs.addTab(self.__all_media_tab, "All Media")

        self.__layout_manager.addWidget(self.__tabs)

    def ____update_media_list_view(self):
        """
        Pulls media list data from DB
        """
        all_media = get_all_media(cursor)

        self.__all_media_view.model().update_item(all_media)


class AbstractMediaTab(QFrame):
    """
    Abstract Class to define shared functionality between the AllMedia and Playlist tabs in the
    main frame.

    DO NOT INSTANTIATE
    """

    def __init__(self, parent: QObject):
        super().__init__(parent)
        self._all_media_view = None

    def _update_media_list_view(self):
        """
        Pulls media list data from DB
        """
        all_media = get_all_media(cursor)

        self._all_media_view.model().update_item(all_media)


class PlaylistTab(AbstractMediaTab):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self.__playlist_view = PlaylistView(self, image_cache)
        self._all_media_view = GenericSubItemListView(self, image_cache)

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

        self.__layout_manager.addWidget(self._all_media_view, 1)
        self.__layout_manager.addStretch()

    def __update_playlist_view(self):
        """
        Pulls playlist data from database and updates UI to reflect the state of the DB
        """

        # Update UI
        self.__playlist_view.relayout()

    # Slots
    @QtCore.pyqtSlot(int)
    def _update_media_list_view(self, playlist_id: int):
        """
        Slot connected to a PlaylistView's should_display_playlist signal

        Retrieves media objects in a playlist and displays them in addMediaView
        """
        super()._update_media_list_view()

        media_list = get_all_media_objects_for_playlist(cursor, playlist_id)
        self._all_media_view.model().update_item(media_list)
        self._all_media_view.update_playlist_id(playlist_id)


class AllMediaTab(AbstractMediaTab):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self._all_media_view = AllMediaListView(self, image_cache)
        self.__filter_view_win = None

        self.__layout_ui()

        self.display_search_button()

    def __layout_ui(self):
        self.__layout_manager.addWidget(self._all_media_view)

        self._update_media_list_view()

    def display_search_button(self):
        layout_button_manager = QHBoxLayout()

        search_button = QPushButton("SEARCH", self)
        search_button.clicked.connect(self.__show_filter_view)
        layout_button_manager.addStretch(0)
        layout_button_manager.addWidget(search_button, 0, Qt.AlignHCenter)
        self.__layout_manager.addLayout(layout_button_manager)

    # Slots
    @QtCore.pyqtSlot()
    def __show_filter_view(self):
        """Slot to show filter view"""

        if self.__filter_view_win:
            """
            We are good programmers, DESTROY memory we stole.
            """
            self.__filter_view_win.destroy()

        # Open FilterView
        self.__filter_view_win = FilterView(self.window())

        # Connect signals to slots
        self.__filter_view_win.should_update_media_list.connect(self.__update_media_list_view)

        show_child_window(self.window(), self.__filter_view_win)

    # Slots
    @QtCore.pyqtSlot(str, float)
    def __update_media_list_view(self, genre_input: str, rating: float):
        """
        Slot connected to a FilterView's display_search_button signal

        Retrieves media objects in a playlist and displays them in addMediaView
        """
        super()._update_media_list_view()

        if genre_input == "---":
            genre = None
        else:
            genre = genre_input

        media_list = get_all_media(cursor, genre, rating)

        self._all_media_view.model().update_item(media_list)
