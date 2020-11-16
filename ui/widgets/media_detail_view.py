"""
This file will define a MediaDetailView.
"""
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QWidget

from ui import image_cache
from ui.widgets.model import media
from ui.widgets.model.entities import Media, Podcast
from ui.image_cache import ImageCache


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
        self.__layout_ui()

    def __layout_ui(self):
        """
        Positions a MediaDetailView's sub-widgets on screen
        """

        self.parentWidget().hide()

        self.setGeometry(0, 0, self.parentWidget().width(), self.parentWidget().height())
        self.setObjectName("details-view")
        self.setWindowTitle("Details")  # FIXME: Make this say type please

        media_name_label = QLabel(self.__media.name)
        media_name_label.setFont(QFont('Arial', 35))
        self.__layout_manager.addWidget(media_name_label, 0, Qt.AlignHCenter)
        self.__layout_manager.addStretch()

    def closeEvent(self, close_event):
        self.parentWidget().show()
        super().closeEvent(close_event)
