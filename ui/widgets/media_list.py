"""
Collates a collection of MediaViews into one MediaList
"""
from typing import Optional

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QModelIndex, Qt, QPoint
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QListView, QAction, QMenu

from backend.handlers import delete_song_from_playlist, cursor, connection, delete_episode_from_playlist, \
    delete_comedy_special_from_playlist, get_all_media_objects_for_playlist
from ui.helper_functions import show_child_window
from ui.image_cache import ImageCache
from ui.widgets.delegate.media_delegate import ItemDelegate
from ui.widgets.media_detail_view import MediaDetailView
from ui.widgets.model.entities import ComedySpecial, Episode, Song
from ui.widgets.model.media_list_model import MediaListModel, AbstractItemListModel, GenericSubItemListModel


class AbstractItemListView(QFrame):
    """
    THIS IS AN ABSTRACT CLASS, DO NOT INSTANTIATE
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent)

        self._image_cache = image_cache

        self._model = AbstractItemListModel(self, image_cache, True)

        self._item_delegate = ItemDelegate(self)

        self._list_view = QListView(self)
        self._list_view.setItemDelegate(self._item_delegate)

        self._layout_manager = QVBoxLayout(self)
        self._layout_ui()

    def _layout_ui(self):
        self._list_view.setSpacing(22)
        self._layout_manager.addWidget(self._list_view)

    def model(self) -> AbstractItemListModel:
        return self._model


class AllMediaListView(AbstractItemListView):
    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache)

        self._model = MediaListModel(self, image_cache)
        self._list_view.setModel(self._model)

        # Connect signals to slots
        self._list_view.doubleClicked.connect(self.__item_double_clicked)
        self._media_detail_win: Optional[MediaDetailView] = None

    @QtCore.pyqtSlot(QModelIndex)
    def __item_double_clicked(self, index: QModelIndex):
        """
        Slot that responds to a user double clicking on any row in the list
        :index: Index of item selected
        """
        media = self._model.at(index.row())

        if self._media_detail_win:
            """
            We are good programmers, DESTROY memory we stole.
            """
            self._media_detail_win.destroy()

        # Open MediaDetailView
        self._media_detail_win = MediaDetailView(self.window(), media)  # We don't want to just hide ourselves, but
        # the whole window
        show_child_window(self.window(), self._media_detail_win)


class GenericSubItemListView(AbstractItemListView):
    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache)

        self._model = GenericSubItemListModel(self, image_cache)
        self._list_view.setModel(self._model)
        self._list_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__playlist_id = 0  # ID of playlist whose contents this list is displaying

        # Connect signals to slots
        self._list_view.customContextMenuRequested.connect(self._show_context_menu)

    def update_playlist_id(self, playlist_id: int):
        self.__playlist_id = playlist_id

    def _remove_item_from_playlist(self, index: QModelIndex):
        """
        Given an index in the list, fetches and removes this playlist from the UI and from the playlist's DB entry
        """
        deletion_item = self._model.at(index.row())

        if type(deletion_item) is Song:
            delete_song_from_playlist(cursor, connection, self.__playlist_id, deletion_item.media_id,
                                      deletion_item.name)
        elif type(deletion_item) is Episode:
            delete_episode_from_playlist(cursor, connection, self.__playlist_id, deletion_item.media_id,
                                         deletion_item.episode_number)
        elif type(deletion_item) is ComedySpecial:
            delete_comedy_special_from_playlist(cursor, connection, self.__playlist_id, deletion_item.media_id)
        else:
            print("Attempt to remove unexpected type from playlist")
            exit(1)

        # TODO: Need to layout UI
        self.relayout()

    def relayout(self):
        """
        Refreshes the UI to reflect the state of the DB
        """
        items = get_all_media_objects_for_playlist(cursor, self.__playlist_id)
        self._model.update_item(items)

    @QtCore.pyqtSlot(QPoint)
    def _show_context_menu(self, pos: QPoint):
        """
        Displays a context menu of user choices on a right-click

        :param pos: Location where user clicked on the screen
        """

        index = self._list_view.indexAt(pos)

        if index.row() != -1:  # Must be a valid index
            global_pos = self._list_view.mapToGlobal(pos)

            context_menu = QMenu(self)

            # User should have the ability to delete from playlist
            del_action = QAction("Remove from this playlist")
            del_action.triggered.connect(lambda: self._remove_item_from_playlist(index))

            context_menu.addAction(del_action)

            context_menu.exec(global_pos)
            del context_menu
