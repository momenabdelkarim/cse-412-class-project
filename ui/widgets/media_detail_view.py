"""
This file will define a MediaDetailView.
"""
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget, QHBoxLayout

from backend.handlers import cursor, get_award, get_person, get_all_songs_in_album, get_episodes_in_podcast, \
    get_organization, get_publisher
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

        # Media Detail View setup
        self.setGeometry(0, 0, self.parentWidget().width(), self.parentWidget().height())
        self.setObjectName("details-view")
        self.setWindowTitle(f"{self.__media.__class__.__name__} Details")  # Display string-name of media object's class

        # Call on layout_header() to display the cover, media name, and persons
        self.__layout_header()

        # Call on display_award_and_org() to show the award and organization for the media
        self.display_award_and_org()

        if type(self.__media) is not ComedySpecial:
            self.__layout_list()

        self.__layout_manager.addStretch()

        # Call on display_footer() to show the genre and rating for the media
        self.display_footer()

    def __layout_header(self):
        """
        Responsible for laying out the album image, album name, and artist
        """
        layout_header_manager = QHBoxLayout()  # used to make a horizontal header
        layout_name_manager = QVBoxLayout()  # used to group media name and person list vertically

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

        # Get media name
        media_name_label = QLabel(self.__media.name)
        media_name_label.setObjectName("media-name")

        # Get list of artists
        artists: List[Person] = get_person(cursor, self.__media.media_id)

        # Create a comma-separated list of artist's names
        artist_names = ""
        for artist in artists:
            artist_names += artist.name + (", " if artist != artists[-1] else "")

        artist_label = QLabel(artist_names)

        # Add media name and artist to layout
        # FIXME: fix the media name and artist left align
        layout_name_manager.addWidget(media_name_label, 0, Qt.AlignLeft)
        layout_name_manager.addWidget(artist_label, 0, Qt.AlignLeft)
        layout_name_manager.addStretch()

        # Add layout_name_manager into the header
        layout_header_manager.addLayout(layout_name_manager)
        layout_header_manager.setObjectName("detail-header")
        layout_header_manager.addStretch(1)

        # Add the header into the outer layout
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

    def display_award_and_org(self):
        """
        Responsible for laying out the won award and organization
        """
        # Display Award information
        if media_awards := get_award(cursor, self.__media.media_id):
            # At this point, we know the media has some amount of awards
            display_award: Award = media_awards[0]
            award_label = QLabel(display_award.award_name, self)
            award_label.setObjectName("award")
            self.__layout_manager.addWidget(award_label, 0, Qt.AlignRight)

            # Display Organization information
            # If there is an award, then there is an organization who gives the award
            organization = get_organization(cursor, display_award.organization_id)
            organization_label = QLabel(organization.name, self)
            organization_label.setObjectName("organization")
            self.__layout_manager.addWidget(organization_label, 0, Qt.AlignRight)

    def display_footer(self):
        """
        Responsible for laying out the genre and rating
        """
        layout_footer_manager = QHBoxLayout()

        genre = self.__media.genre
        rating = self.__media.rating
        publisher = get_publisher(cursor, self.__media.media_id)

        genre_label = QLabel(genre.upper(), self)
        genre_label.setObjectName("genre")
        rating_label = QLabel(f"{rating}", self)
        rating_label.setObjectName("rating")
        publisher_label = QLabel(publisher.name, self)
        publisher_label.setObjectName("publisher")

        layout_footer_manager.addWidget(genre_label, 0, Qt.AlignHCenter)
        layout_footer_manager.addWidget(rating_label, 0, Qt.AlignHCenter)
        layout_footer_manager.addWidget(publisher_label, 0, Qt.AlignHCenter)

        self.__layout_manager.addLayout(layout_footer_manager)