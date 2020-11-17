from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QModelIndex, Qt, QPoint
from PyQt5.QtWidgets import QFrame, QListView, QVBoxLayout, QMenu, QAction

from ui.image_cache import ImageCache
from ui.widgets.delegate.media_delegate import ItemDelegate
from ui.widgets.model.media_list_model import SongListModel, EpisodeListModel, AbstractItemListModel


class AbstractSubItemListView(QFrame):
    """
    THIS IS AN ABSTRACT CLASS, DO NOT INSTANTIATE
    """

    def __init__(self, parent: QObject, image_cache: ImageCache, is_playlist_view: bool):
        super().__init__(parent)

        self._image_cache = image_cache
        self._is_playlist_view = is_playlist_view  # Whether or not this list is embedded in a playlist view
        self._model = AbstractItemListModel(self, image_cache, True)

        self._item_delegate = ItemDelegate(self)

        self._list_view = QListView(self)
        self._list_view.setItemDelegate(self._item_delegate)
        self._list_view.setContextMenuPolicy(Qt.CustomContextMenu)

        self._layout_manager = QVBoxLayout(self)
        self._layout_ui()

        # Connect signals to slots
        self._list_view.customContextMenuRequested.connect(self._show_context_menu)

    def _layout_ui(self):
        self._list_view.setSpacing(22)
        self._layout_manager.addWidget(self._list_view)

    def model(self) -> AbstractItemListModel:
        return self._model

    def _remove_item_from_playlist(self, index: QModelIndex):
        """
        Given an index in the list, fetches and removes this playlist from the UI and from the playlist's DB entry
        """
        pass

    def _add_item_to_playlist(self, index: QModelIndex):
        """
        Given an index in the list, allows the user to add the selected item to a playlist of their choice
        """
        pass

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

            if self._is_playlist_view:
                # User should have the ability to delete from playlist
                del_action = QAction("Remove from this playlist")
                del_action.triggered.connect(lambda: self._remove_item_from_playlist(index))

                context_menu.addAction(del_action)

            else:
                # User should have the ability to add to playlist
                add_action = QAction("Add to playlist")
                add_action.triggered.connect(lambda: self._add_item_to_playlist(index))

                context_menu.addAction(add_action)

            context_menu.exec(global_pos)
            del context_menu


class SongListView(AbstractSubItemListView):
    """
    This class lays out the view of list of songs in an album
    """

    def __init__(self, parent: QObject, image_cache: ImageCache, is_playlist_view: bool):
        super().__init__(parent, image_cache, is_playlist_view)

        self._model = SongListModel(self, image_cache)
        self._list_view.setModel(self._model)


class EpisodeListView(AbstractSubItemListView):
    """
    This class lays out the view of list of songs in an album
    """

    def __init__(self, parent: QObject, image_cache: ImageCache, is_playlist_view: bool):
        super().__init__(parent, image_cache, is_playlist_view)

        self._model = EpisodeListModel(self, image_cache)
        self._list_view.setModel(self._model)
