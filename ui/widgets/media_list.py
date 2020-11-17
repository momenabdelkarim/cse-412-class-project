"""
Collates a collection of MediaViews into one MediaList
"""
from typing import Optional

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QModelIndex
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QListView

from ui.helper_functions import show_child_window
from ui.image_cache import ImageCache
from ui.widgets.delegate.media_delegate import ItemDelegate
from ui.widgets.media_detail_view import MediaDetailView
from ui.widgets.model.media_list_model import MediaListModel, AbstractItemListModel


class AbstractItemListView(QFrame):
    """
    THIS IS AN ABSTRACT CLASS, DO NOT INSTANTIATE
    """

    def __init__(self, parent: QObject, image_cache: ImageCache, is_playlist_view: bool):
        super().__init__(parent)

        self._image_cache = image_cache
        self._is_playlist_view = is_playlist_view

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


class AddMediaListView(AbstractItemListView):
    def __init__(self, parent: QObject, image_cache: ImageCache, is_playlist_view: bool):
        super().__init__(parent, image_cache, is_playlist_view)

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
        self._media_detail_win = MediaDetailView(self.window(), media,
                                                 self._is_playlist_view)  # We don't want to just hide ourselves, but
        # the whole window
        show_child_window(self.window(), self._media_detail_win)
