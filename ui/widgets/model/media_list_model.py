"""
Defines the model of a MediaList, to be used with a QListView
"""
from typing import List, Any, Dict

from PyQt5.QtCore import QAbstractListModel, QObject, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QPixmap

from ui.image_requester import ImageRequester
from ui.widgets.model.media import Media


class MediaListModel(QAbstractListModel):
    """
    A media list holds a collection of multimedia, displaying an optional photo, title, and subtitle.
    """

    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__media_list: List[Media] = list()  # Tracks all multimedia items being displayed in this list
        self.__image_requester = ImageRequester(self)
        self.__pix_cache: Dict[str: QPixmap] = dict()  # Track pixmaps that have already been resolved by ImageRequester

        # Connect signals to slots
        self.__image_requester.image_request_finished.connect(self.__handle_icon_response)

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
            if cached_pix := self.__pix_cache.get(media.photo_url()):
                return cached_pix
            else:
                # Set default pixmap and asynchronously request actual image via HTTP
                self.__image_requester.request(media.photo_url())
                return QPixmap(R"img/default_photo.png")
        else:
            return QVariant()

    # Slots
    def __handle_icon_response(self, url: str, pix: QPixmap):
        """
        Handles an image request response from ImageRequester
        """
        self.__pix_cache[url] = pix
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    # Exposed functionality

    def add_media(self, media: Media):
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
