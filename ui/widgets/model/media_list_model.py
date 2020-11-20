"""
Defines the model of a MediaList, to be used with a QListView
"""
from typing import Any

from PyQt5.QtCore import QAbstractListModel, QObject, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QPixmap

from backend.handlers import cursor, get_guest
from ui.helper_functions import convert_pixmap_to_circular
from ui.image_cache import ImageCache
from ui.widgets.model.entities import Episode, Song, ComedySpecial


class AbstractItemListModel(QAbstractListModel):
    """
    THIS IS AN ABSTRACT CLASS, DO NOT INSTANTIATE
    """

    def __init__(self, parent: QObject, image_cache: ImageCache, displays_image: bool):
        super().__init__(parent)
        self._item_list = list()  # Track all items being displayed in this list
        self._image_cache = image_cache
        self.displays_image = displays_image

        # Connect signals to slots
        self._image_cache.new_image_resolved.connect(lambda: self.dataChanged.emit(QModelIndex(), QModelIndex()))

    # Overrides
    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._item_list)

    def add_item(self, item):
        """
        Adds the given media item to the list of media
        """
        insertion_idx = self.rowCount()
        self.beginInsertRows(QModelIndex(), insertion_idx, insertion_idx)
        self._item_list.append(item)
        self.endInsertRows()

    def at(self, row: int) -> Any:
        if row < self.rowCount():
            return self._item_list[row]
        else:
            return QVariant()

    def update_item(self, new_item_list):
        """
        Update the media list to reflect state of DB
        :param new_item_list: List of media objects in the DB
        """
        self._item_list.clear()
        for item in new_item_list:
            self.add_item(item)


class MediaListModel(AbstractItemListModel):
    """
    A media list holds a collection of multimedia, displaying an optional photo, title, and subtitle.
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache, True)
        self.__image_diameter = 100

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() >= self.rowCount():
            return QVariant()

        media = self._item_list[index.row()]
        if role == Qt.DisplayRole:
            return media.name
        elif role == Qt.DecorationRole:
            if cached_pix := self._image_cache.get_pixmap(media.cover_url):
                return convert_pixmap_to_circular(cached_pix, self.__image_diameter)
            else:
                # Set default pixmap and asynchronously request actual image via HTTP
                self._image_cache.request_url(media.cover_url)
                return QPixmap(R"img/default_photo.png")
        elif role == Qt.UserRole:
            return media.genre
        else:
            return QVariant()


class SongListModel(AbstractItemListModel):
    """
    A song list holds a collection of songs belonging to an album object
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache, False)

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() >= self.rowCount():
            return QVariant()

        song = self._item_list[index.row()]
        if role == Qt.DisplayRole:
            return song.name
        elif role == Qt.DecorationRole:
            return None
        elif role == Qt.UserRole:
            return f"{song.duration}s, {song.view_count} views"
        else:
            return QVariant()


class EpisodeListModel(AbstractItemListModel):
    """
    An episode list model holds a collection of episodes belonging to a podcast object
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache, False)

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() >= self.rowCount():
            return QVariant()

        episode = self._item_list[index.row()]
        if role == Qt.DisplayRole:
            if guests := get_guest(cursor, episode.media_id, episode.episode_number):
                return f"{episode.name} (Ft. {', '.join(guests)})"
            else:
                return episode.name
        elif role == Qt.UserRole:
            return f"Episode {episode.episode_number}: {episode.duration}s, {episode.view_count} views"
        else:
            return QVariant()


class ComedySpecialListModel(AbstractItemListModel):
    """
    A comedy special list model holds a collection of ComedySpecials in a ComedySpecial
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache, False)

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() >= self.rowCount():
            return QVariant()

        special = self._item_list[index.row()]
        if role == Qt.DisplayRole:
            return special.name
        elif role == Qt.UserRole:
            return f"{special.runtime}m, originally performed at {special.venue}"
        else:
            return QVariant()


class GenericSubItemListModel(AbstractItemListModel):
    """
    An episode list model holds a collection of episodes belonging to a podcast object
    """

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent, image_cache, False)

    def data(self, index: QModelIndex, role: int = ...) -> Any:

        # Guard against invalid row subscripting
        if not index.isValid() or index.row() >= self.rowCount():
            return QVariant()

        sub_item = self._item_list[index.row()]
        if role == Qt.DisplayRole:
            if type(sub_item) is Episode:
                if guests := get_guest(cursor, sub_item.media_id, sub_item.episode_number):
                    return f"{sub_item.name} (Ft. {', '.join(guests)})"
                else:
                    return sub_item.name
            else:
                return sub_item.name
        elif role == Qt.UserRole:
            if type(sub_item) is Episode:
                return f"Episode {sub_item.episode_number}: {sub_item.duration}s, {sub_item.view_count} views"
            elif type(sub_item) is Song:
                return f"{sub_item.duration}s, {sub_item.view_count} views"
            elif type(sub_item) is ComedySpecial:
                return f"{sub_item.runtime}m, originally performed at {sub_item.venue}"
            else:
                print("Unexpected media list model type encountered")
                exit(1)
        else:
            return QVariant()
