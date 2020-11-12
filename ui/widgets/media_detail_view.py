"""
This file will define a MediaDetailView.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel

from ui.widgets.model.entities import Media


class MediaDetailView(QFrame):
    """
    A MediaDetailView displays the items in an Auditory Media object (if they exist)
    It will also display the attributes of an Auditory Media object.
    """

    def __init__(self, media: Media):
        super().__init__(None)  # Create as a standalone window

        self.__layout_manager = QVBoxLayout(self)
        self.__media = media
        self.__layout_ui()

    def __layout_ui(self):
        """
        Positions a MediaDetailView's sub-widgets on screen
        """
        self.setGeometry(0, 0, 800, 700)
        self.setObjectName("details-view")
        self.setWindowTitle("Details")  # FIXME: Make this say type please

        test_label = QLabel(self.__media.name)
        self.__layout_manager.addWidget(test_label, 0, Qt.AlignHCenter)
        self.__layout_manager.addStretch()
