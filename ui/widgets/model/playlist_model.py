"""
Defines the model of a PlaylistView
"""
import re
from typing import List, Any

from PyQt5.QtCore import QAbstractListModel, QObject, QModelIndex, QVariant, Qt
from PyQt5.QtGui import QPixmap, QColor

from backend.handlers import get_all_media_objects_for_playlist, cursor, delete_playlist, connection, \
    create_new_playlist, get_all_user_playlists, get_album_for_selected_song, get_podcast_for_selected_episode
from ui.helper_functions import tile_pixmaps, colorize_pixmap
from ui.image_cache import ImageCache
from ui.widgets.model.entities import Playlist, Song, Episode, ComedySpecial


class PlaylistModel(QAbstractListModel):
    DEFAULT_OWNER_NAME = "Me"

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent)

        self.__playlists: List[Playlist] = [Playlist(-1, "Create Playlist")]  # Should always have a add playlist button
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
            return playlist.name
        elif role == Qt.DecorationRole:
            if index.row() == len(self.__playlists) - 1:
                # This is the add button
                return colorize_pixmap(R"img/plus.svg", QColor(29, 185, 84))

            # Create icon containing either a random media's icon or 4 tiled
            playlist_media = get_all_media_objects_for_playlist(cursor, playlist.playlist_id)
            album_art = self.__get_album_art_for_playlist(playlist_media)

            media_count = len(album_art)
            if media_count == 0:
                # Return a default
                return QPixmap(R"img/default_photo.png")
            elif media_count < 4:
                # Return a random icon
                rand_media = album_art[0]
                if pix := self.__image_cache.get_pixmap(rand_media):
                    return pix
                else:
                    self.__image_cache.request_url(rand_media)
                    return QPixmap(R"img/default_photo.png")
            elif media_count >= 4:
                # Return a tile of any four icons
                indices = range(4)
                pixmaps: List[QPixmap] = list()

                for idx in indices:
                    media_item = album_art[idx]

                    if resolved_pix := self.__image_cache.get_pixmap(media_item):
                        pixmaps.append(resolved_pix)
                    else:
                        self.__image_cache.request_url(media_item)
                        pixmaps.append(QPixmap(R"img/default_photo.png"))

                return tile_pixmaps(pixmaps, 150)
        else:
            return QVariant()

    def create_new_playlist(self):
        """
        Add a new playlist to UI and DB
        """

        temp_playlist_name = f"Playlist {self.__get_incremented_playlist_number()}"
        create_new_playlist(cursor, connection, temp_playlist_name, PlaylistModel.DEFAULT_OWNER_NAME)

        self.update_playlist(get_all_user_playlists(cursor))

    def add_playlist(self, playlist: Playlist):
        """
        Add a new playlist to UI ONLY (For Display)
        :param playlist: Playlist to be added
        """

        insertion_idx = self.rowCount() - 1  # Always insert before the addition button
        self.beginInsertRows(QModelIndex(), insertion_idx, insertion_idx)
        self.__playlists.insert(insertion_idx, playlist)
        self.endInsertRows()

    def delete_playlist(self, deletion_idx: QModelIndex):
        """
        Delete a playlist from the UI and DB
        """
        del_row = deletion_idx.row()
        self.beginRemoveRows(QModelIndex(), del_row, del_row)
        removed_playlist: Playlist = self.__playlists.pop(del_row)
        delete_playlist(cursor, connection, removed_playlist.playlist_id)
        self.endRemoveRows()

    def at(self, row: int) -> Any:
        if row < self.rowCount():
            return self.__playlists[row]
        else:
            return QVariant()

    def update_playlist(self, new_playlists: List[Playlist]):
        """
        Updates the model to reflect a newly requested list of playlists from the DB
        """
        add_button = self.__playlists[-1]

        self.beginRemoveRows(QModelIndex(), 0, self.rowCount())
        self.__playlists.clear()
        self.endRemoveRows()

        self.__playlists.append(add_button)
        for playlist in new_playlists:
            self.add_playlist(playlist)

    def __get_incremented_playlist_number(self):
        """
        Not for external use, should loop through all currently displayed playlists and find the highest Playlist #

        and return # + 1
        """

        selection_regex = re.compile(r'Playlist ([0-9]+)')
        highest_numbered_playlist = 0
        for playlist in self.__playlists:
            if match := selection_regex.search(playlist.name):
                highest_numbered_playlist = int(match.group(1))
        return highest_numbered_playlist + 1

    def __get_album_art_for_playlist(self, playlist_contents: List) -> List[str]:
        """
        Returns a deterministic list of all unique album art associated with each playlist item
        """

        album_cover_url_set = set()

        for item in playlist_contents:
            if type(item) is Song:
                media = get_album_for_selected_song(cursor, item.media_id)
            elif type(item) is Episode:
                media = get_podcast_for_selected_episode(cursor, item.media_id)
            elif type(item) is ComedySpecial:
                media = item
            else:
                print("Encountered unexpected item type in playlist_model")
                exit(1)

            album_cover_url_set.add(media.cover_url)

        return sorted(album_cover_url_set)
