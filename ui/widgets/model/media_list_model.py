"""
Defines the model of a MediaList, to be used with a QListView
"""
from typing import List, Any

from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractListModel, QObject, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QPixmap

from ui.helper_functions import convert_pixmap_to_circular
from ui.image_cache import ImageCache
from ui.widgets.model.media import DebugMedia


class MediaListModel(QAbstractListModel):
    """
    A media list holds a collection of multimedia, displaying an optional photo, title, and subtitle.
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent)
        self.__media_list: List[DebugMedia] = list()  # Tracks all multimedia items being displayed in this list
        self.__image_cache = image_cache
        self.__image_diameter = 100

        # Connect signals to slots
        self.__image_cache.new_image_resolved.connect(lambda: self.dataChanged.emit(QModelIndex(), QModelIndex()))

    # Overrides
    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__media_list)

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() > self.rowCount():
            return QVariant()

        media = self.__media_list[index.row()]
        if role == Qt.DisplayRole:
            return media.title()
        elif role == Qt.DecorationRole:
            if cached_pix := self.__image_cache.get_pixmap(media.photo_url()):
                return convert_pixmap_to_circular(cached_pix, self.__image_diameter)
            else:
                # Set default pixmap and asynchronously request actual image via HTTP
                self.__image_cache.request_url(media.photo_url())
                return QPixmap(R"img/default_photo.png")
        else:
            return QVariant()

    # Exposed functionality

    def add_media(self, media: DebugMedia):
        """
        Adds the given media item to the list of media
        """
        insertion_idx = self.rowCount()
        self.beginInsertRows(QModelIndex(), insertion_idx, insertion_idx)
        self.__media_list.append(media)
        self.endInsertRows()

    def at(self, row: int) -> Any:
        if row < self.rowCount():
            return self.__media_list[row]
        else:
            return QVariant()
