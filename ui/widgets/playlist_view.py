from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal, QModelIndex, Qt, QPoint
from PyQt5.QtWidgets import QListView, QVBoxLayout, QFrame, QMenu, QAction, QDialog

from backend.handlers import rename_playlist, cursor, connection, get_all_user_playlists
from ui.image_cache import ImageCache
from ui.widgets.delegate.playlist_delegate import PlaylistDelegate
from ui.widgets.dialogs import RenamePlaylistDialog
from ui.widgets.model.playlist_model import PlaylistModel


class PlaylistView(QFrame):
    """
    Horizontal Scroll Area containing playlists that can be selected
    """

    # Signals
    should_display_playlist = pyqtSignal(int)  # Display playlist given playlist_id

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent)

        self.__item_delegate = PlaylistDelegate(self)
        self.__model = PlaylistModel(self, image_cache)

        self.__horizontal_list = QListView(self)
        self.__horizontal_list.setModel(self.__model)
        self.__horizontal_list.setItemDelegate(self.__item_delegate)
        self.__horizontal_list.verticalScrollBar().setEnabled(False)
        self.__horizontal_list.setContextMenuPolicy(Qt.CustomContextMenu)

        self.__layout_manager = QVBoxLayout(self)
        self.__layout_ui()

        # Connect signals to slots
        self.__horizontal_list.doubleClicked.connect(self.__playlist_double_clicked)
        self.__horizontal_list.customContextMenuRequested.connect(self.__show_context_menu)

    def __layout_ui(self):
        # Set up horizontal list
        self.__horizontal_list.setFlow(QListView.LeftToRight)
        self.__horizontal_list.setMinimumHeight(235)
        self.__horizontal_list.setSpacing(20)
        self.__layout_manager.addWidget(self.__horizontal_list)

    def model(self) -> PlaylistModel:
        return self.__model

    @QtCore.pyqtSlot(QModelIndex)
    def __playlist_double_clicked(self, index: QModelIndex):
        """
        Slot that connects to the doubleClicked signal

        Should either display contents of the playlist or allow for playlist creation (index dependent)
        :index: Index that was clicked
        """
        should_create_playlist = (index.row() != self.__model.rowCount() - 1)
        if should_create_playlist:
            # Didn't click last index (create playlist), should display contents
            self.should_display_playlist.emit(self.__model.at(index.row()).playlist_id)
        else:
            self.__model.create_new_playlist()

    @QtCore.pyqtSlot(QModelIndex)
    def __handle_playlist_rename(self, index: QModelIndex):
        """
        Allows the user to rename the playlist at index
        """
        playlist = self.__model.at(index.row())
        rename_dialog = RenamePlaylistDialog(self, playlist)
        if rename_dialog.exec() == QDialog.Accepted:
            # Rename successfully requested
            new_playlist_name = rename_dialog.get_new_name()
            rename_playlist(cursor, connection, playlist.playlist_id, new_playlist_name)
            self.relayout()

    @QtCore.pyqtSlot(QPoint)
    def __show_context_menu(self, pos: QPoint):
        """
        Displays a context menu of user choices on a right-click

        :param pos: Location where user clicked on the screen
        """

        index = self.__horizontal_list.indexAt(pos)

        if index.row() != -1 and index.row() != self.__model.rowCount() - 1:  # Must be a valid index and not create
            global_pos = self.__horizontal_list.mapToGlobal(pos)

            context_menu = QMenu(self)

            show_action = QAction("Show Playlist")
            show_action.triggered.connect(lambda: self.__playlist_double_clicked(index))

            rename_action = QAction("Rename Playlist")
            rename_action.triggered.connect(lambda: self.__handle_playlist_rename(index))

            del_action = QAction("Delete Playlist")
            del_action.triggered.connect(lambda: self.__horizontal_list.model().delete_playlist(index))

            context_menu.addAction(show_action)
            context_menu.addSeparator()
            context_menu.addAction(rename_action)
            context_menu.addAction(del_action)

            context_menu.exec(global_pos)
            del context_menu

    def relayout(self):
        """
        Refreshes the UI to reflect the state of the DB
        """
        playlists = get_all_user_playlists(cursor)
        self.__model.update_playlist(playlists)
