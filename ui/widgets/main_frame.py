"""
Defines the application's main view
"""
from typing import Optional

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFrame, QTabWidget, QVBoxLayout

from ui.image_cache import ImageCache
from ui.widgets.media_list import AddMediaListView
from ui.widgets.model.media import DebugMedia, DebugPlaylist
from ui.widgets.model.media_list_model import MediaListModel
from ui.widgets.playlist_view import PlaylistView

image_cache: Optional[ImageCache] = None

def build_debug_media_list(parent: QObject) -> AddMediaListView:
    colter_album = DebugMedia("Imaginary Appalachia", "Colter Wall",
                              "https://www.outhousetickets.com/Artist/3807/photo/colter-wall-event.png")
    tom_special = DebugMedia("Mostly Stories", "Tom Segura",
                             "https://images-na.ssl-images-amazon.com/images/I/71XbjhskX0L._SL1500_.jpg")
    joe_podcast = DebugMedia("The Joe Rogan Experience #1169", "Joe Rogan Ft. Elon Musk",
                             "https://i.ytimg.com/vi/ycPr5-27vSI/sddefault.jpg")

    DEBUG_MEDIA_LIST = AddMediaListView(parent, image_cache)
    DEBUG_MEDIA_LIST.model().add_media(colter_album)
    DEBUG_MEDIA_LIST.model().add_media(tom_special)
    DEBUG_MEDIA_LIST.model().add_media(joe_podcast)

    return DEBUG_MEDIA_LIST


def build_debug_playlist_list(parent: QObject) -> PlaylistView:
    p1 = DebugPlaylist("Little Bit of Everything", "Lily")
    p2 = DebugPlaylist("My Music", "Joe")
    p3 = DebugPlaylist("Standup Comedy", "Steve")
    p4 = DebugPlaylist("My Podcasts", "Mary")

    joe_podcast = DebugMedia("The Joe Rogan Experience #1169", "Joe Rogan Ft. Elon Musk",
                             "https://i.ytimg.com/vi/ycPr5-27vSI/sddefault.jpg")
    darknet_podcast = DebugMedia("Darknet Diaries", "Jack Rhysider",
                                 "https://upload.wikimedia.org/wikipedia/en/6/6a/Darknet_Diaries_podcast_artwork.jpg")
    cleared_podcast = DebugMedia("Cleared Hot", "Andy Stumpf",
                                 "https://ssl-static.libsyn.com/p/assets/5/2/8/8/5288b59023ee5e17/cleared_hot_thumbnail.jpg")
    jordan_podcast = DebugMedia("The Jordan Harbinger Show", "Jordan Harbinger",
                                "https://www.jordanharbinger.com/wp-content/uploads/2020/04/2020-Showart-updated-with-PC1-logo-Large.png")

    bob_album = DebugMedia("Uprising", "Bob Marley and the Wailers",
                           "https://images-na.ssl-images-amazon.com/images/I/71NZGTFf3pL._SX466_.jpg")
    tyler_album = DebugMedia("Country Squire", "Tyler Childers",
                             "https://images-na.ssl-images-amazon.com/images/I/8117Ud8vwbL._SY355_.jpg")
    colter_album = DebugMedia("Imaginary Appalachia", "Colter Wall",
                              "https://www.outhousetickets.com/Artist/3807/photo/colter-wall-event.png")
    hotel_album = DebugMedia("Hotel California", "The Eagles",
                             "https://images-na.ssl-images-amazon.com/images/I/71SQ5kO9hIL._SX466_.jpg")

    bill_comedy = DebugMedia("Paper Tiger", "Bill Burr",
                             "https://radradio.com/wp-content/uploads/billburr-papertiger-951x634.jpg")
    dave_comedy = DebugMedia("Equanimity", "Dave Chappelle",
                             "https://m.media-amazon.com/images/M/MV5BODJkMTAxNmYtZDg4OS00NzA2LTlmZTUtMDc2MjIwMzE4ZDMxXkEyXkFqcGdeQXVyMTk3NDAwMzI@._V1_.jpg")
    tom_special = DebugMedia("Mostly Stories", "Tom Segura",
                             "https://images-na.ssl-images-amazon.com/images/I/71XbjhskX0L._SL1500_.jpg")
    joe_special = DebugMedia("Strange Times", "Joe Rogan",
                             "https://images-na.ssl-images-amazon.com/images/I/81DBwOq5jWL._SL1500_.jpg")

    p1.add(bob_album)
    p1.add(tyler_album)
    p1.add(bill_comedy)
    p1.add(joe_podcast)

    p2.add(tyler_album)
    p2.add(colter_album)
    p2.add(hotel_album)
    p2.add(bob_album)

    p3.add(bill_comedy)
    p3.add(dave_comedy)
    p3.add(tom_special)
    p3.add(joe_special)

    p4.add(cleared_podcast)
    p4.add(joe_podcast)
    p4.add(jordan_podcast)
    p4.add(darknet_podcast)

    p_view = PlaylistView(parent, image_cache)
    p_view.model().add_playlist(p1)
    p_view.model().add_playlist(p2)
    p_view.model().add_playlist(p3)
    p_view.model().add_playlist(p4)

    return p_view


class MainFrame(QFrame):

    def __init__(self, parent: QObject):
        global image_cache
        image_cache = ImageCache(parent)

        super().__init__(parent)

        self.__tabs = QTabWidget(self)
        self.__playlist_tab = PlaylistTab(self)
        self.__add_media_tab = AddMediaTab(self)
        self.__layout_manager = QVBoxLayout(self)

        self.__layout_ui()

    def __layout_ui(self):
        # Set up tabs
        self.__tabs.addTab(self.__playlist_tab, "My Playlists")
        self.__tabs.addTab(self.__add_media_tab, "All Media")

        self.__layout_manager.addWidget(self.__tabs)


class PlaylistTab(QFrame):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self.__playlist_view = build_debug_playlist_list(self)
        self.__add_media_view = build_debug_media_list(self)

        self.__layout_ui()

    def __layout_ui(self):
        self.__layout_manager.addWidget(self.__playlist_view)

        # Add dividing line
        line = QFrame(self)
        line.setObjectName("line")
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.__layout_manager.addWidget(line)

        self.__layout_manager.addWidget(self.__add_media_view, 1)
        self.__layout_manager.addStretch()

class AddMediaTab(QFrame):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__layout_manager = QVBoxLayout(self)
        self.__add_media_view = build_debug_media_list(self)

        self.__layout_ui()

    def __layout_ui(self):
        self.__layout_manager.addWidget(self.__add_media_view)
