"""
This file will define a MediaDetailView.
"""
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget, QHBoxLayout

from backend.handlers import cursor, get_award, get_person, get_all_songs_in_album, get_episodes_in_podcast
from ui.helper_functions import convert_pixmap_to_circular
from ui.image_cache import image_cache
from ui.widgets.model.entities import Media, Award, Person, ComedySpecial, Album, Podcast
from ui.widgets.sub_list import EpisodeListView, SongListView


class MediaDetailView(QFrame):
    """
    A MediaDetailView displays the items in an Auditory Media object (if they exist)
    It will also display the attributes of an Auditory Media object.
    """

    def __init__(self, parent_window: QWidget, media: Media):
        super().__init__(parent_window)  # Create as a standalone window
        self.setWindowFlag(Qt.Window)

        self.__layout_manager = QVBoxLayout(self)
        self.__media = media
        self.__item_list = None
        self.__layout_ui()

    def __layout_ui(self):
        """
        Positions a MediaDetailView's sub-widgets on screen
        """

        self.parentWidget().hide()

        self.setGeometry(0, 0, self.parentWidget().width(), self.parentWidget().height())
        self.setObjectName("details-view")
        self.setWindowTitle(f"{self.__media.__class__.__name__} Details")  # Display string-name of media object's class

        self.__layout_header()

        # Layout Award Information
        if media_awards := get_award(cursor, self.__media.media_id):
            # At this point, we know the media has some amount of awards
            display_award: Award = media_awards[0]
            award_label = QLabel(display_award.award_name, self)
            award_label.setObjectName("award")
            self.__layout_manager.addWidget(award_label, 0, Qt.AlignRight)

        if type(self.__media) is not ComedySpecial:
            self.__layout_list()

        self.__layout_manager.addStretch()

    def __layout_header(self):
        """
        Responsible for laying out the album image, album name, and artist
        """
        layout_header_manager = QHBoxLayout()
        layout_name_manager = QVBoxLayout()

        # Display Album Photo
        if cached_pix := image_cache.get_pixmap(self.__media.cover_url):
            pix = convert_pixmap_to_circular(cached_pix, 300)
        else:
            # Set default pixmap and asynchronously request actual image via HTTP
            image_cache.request_url(self.__media.cover_url)
            pix = QPixmap(R"img/default_photo.png")

        image_label = QLabel(self)
        image_label.setPixmap(pix)
        layout_header_manager.addWidget(image_label)

        # Display album name
        media_name_label = QLabel(self.__media.name)
        media_name_label.setObjectName("media-name")

        # Display artist name
        artists: List[Person] = get_person(cursor, self.__media.media_id)

        # Create a comma-separated list of artist's names
        artist_names = ""
        for artist in artists:
            artist_names += artist.name + (", " if artist != artists[-1] else "")

        artist_label = QLabel(artist_names)
        layout_name_manager.addWidget(media_name_label)
        layout_name_manager.addWidget(artist_label)
        layout_name_manager.addStretch()

        layout_header_manager.addLayout(layout_name_manager)
        layout_header_manager.addStretch(1)
        layout_header_manager.setObjectName("detail-header")
        self.__layout_manager.addLayout(layout_header_manager)

    def __layout_list(self):
        """
        This function is responsible for laying out the list of items and their attributes in the media
        """

        # Get all items in the media object and create list
        if type(self.__media) is Album:
            media_items = get_all_songs_in_album(cursor, self.__media.media_id)
            self.__item_list = SongListView(self, image_cache)
        elif type(self.__media) is Podcast:
            media_items = get_episodes_in_podcast(cursor, self.__media.media_id)
            self.__item_list = EpisodeListView(self, image_cache)
        else:
            print("Something has gone horribly wrong")
            exit(1)

        # Display the list
        self.__item_list.model().update_item(media_items)
        self.__layout_manager.addWidget(self.__item_list, 1)

    def closeEvent(self, close_event):
        self.parentWidget().show()
        super().closeEvent(close_event)
