from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QModelIndex
from PyQt5.QtWidgets import QFrame, QListView, QVBoxLayout

from ui.image_cache import ImageCache
from ui.widgets.delegate.media_delegate import ItemDelegate
from ui.widgets.model.media_list_model import SongListModel, EpisodeListModel, AbstractItemListModel


class AbstractSubItemListView(QFrame):
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


class SongListView(AbstractSubItemListView):
    """
    This class lays out the view of list of songs in an album
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache)

        self._model = SongListModel(self, image_cache)
        self._list_view.setModel(self._model)

        # Connect signals to slots
        self._list_view.doubleClicked.connect(self.__item_double_clicked)

    @QtCore.pyqtSlot(QModelIndex)
    def __item_double_clicked(self, index: QModelIndex):
        """
        Slot that responds to a user double clicking on any row in the list
        :index: Index of item selected
        """
        print("Clicked!")


class EpisodeListView(AbstractSubItemListView):
    """
    This class lays out the view of list of songs in an album
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache)

        self._model = EpisodeListModel(self, image_cache)
        self._list_view.setModel(self._model)
        # self._list_view.setSpacing(35)

        # Connect signals to slots
        self._list_view.doubleClicked.connect(self.__item_double_clicked)

    @QtCore.pyqtSlot(QModelIndex)
    def __item_double_clicked(self, index: QModelIndex):
        """
        Slot that responds to a user double clicking on any row in the list
        :index: Index of item selected
        """
        print("Clicked!")
