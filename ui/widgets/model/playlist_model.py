"""
Defines the model of a PlaylistView
"""
from typing import List, Any

from PyQt5.QtCore import QAbstractListModel, QObject, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QPixmap

from ui.helper_functions import tile_pixmaps
from ui.image_cache import ImageCache
from ui.widgets.model.entities import Playlist


class PlaylistModel(QAbstractListModel):
    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent)

        self.__playlists: List[DebugPlaylist] = list()
        self.__image_cache = image_cache

        # Connect signals to slots
        self.__image_cache.new_image_resolved.connect(lambda: self.dataChanged.emit(QModelIndex(), QModelIndex()))

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.__playlists)

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() > self.rowCount():
            return QVariant()

        playlist = self.__playlists[index.row()]
        if role == Qt.DisplayRole:
            return playlist.title()
        elif role == Qt.DecorationRole:
            # Create icon containing either a random media's icon or 4 tiled
            media_count = len(playlist.media())
            if media_count == 0:
                # Return a default
                return QPixmap(R"img/default_photo.png")
            elif media_count < 4:
                # Return a random icon
                rand_media = playlist.media()[0]
                if pix := self.__image_cache.get_pixmap(rand_media.photo_url()):
                    return pix
                else:
                    self.__image_cache.request_url(rand_media.photo_url())
                    return QPixmap(R"img/default_photo.png")
            elif media_count >= 4:
                # Return a tile of any four icons
                indices = range(4)
                pixmaps: List[QPixmap] = list()

                for idx in indices:
                    media_item = playlist.media()[idx]

                    if resolved_pix := self.__image_cache.get_pixmap(media_item.photo_url()):
                        pixmaps.append(resolved_pix)
                    else:
                        self.__image_cache.request_url(media_item.photo_url())
                        pixmaps.append(QPixmap(R"img/default_photo.png"))

                return tile_pixmaps(pixmaps, 150)
        else:
            return QVariant()

    def add_playlist(self, playlist: Playlist):
        insertion_idx = self.rowCount()
        self.beginInsertRows(QModelIndex(), insertion_idx, insertion_idx)
        self.__playlists.append(playlist)
        self.endInsertRows()

    def at(self, row: int) -> Any:
        if row < self.rowCount():
            return self.__playlists[row]
        else:
            return QVariant()
