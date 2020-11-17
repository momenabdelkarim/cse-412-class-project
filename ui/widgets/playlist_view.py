from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QListView, QVBoxLayout, QFrame

from ui.image_cache import ImageCache
from ui.widgets.delegate.playlist_delegate import PlaylistDelegate
from ui.widgets.model.playlist_model import PlaylistModel


class PlaylistView(QFrame):
    """
    Horizontal Scroll Area containing playlists that can be selected
    """

    # Signals
    should_display_playlist = pyqtSignal(int)  # Display playlist given playlist_id

    def __init__(self, parent: QObject, image_cache: ImageCache):
        super().__init__(parent)

        self.__item_delegate = PlaylistDelegate(self)
        self.__model = PlaylistModel(self, image_cache)

        self.__horizontal_list = QListView(self)
        self.__horizontal_list.setModel(self.__model)
        self.__horizontal_list.setItemDelegate(self.__item_delegate)
        self.__horizontal_list.verticalScrollBar().setEnabled(False)

        self.__layout_manager = QVBoxLayout(self)
        self.__layout_ui()

        # Connect signals to slots
        self.__horizontal_list.doubleClicked.connect(lambda index:
                                                     self.should_display_playlist.emit(
                                                         self.__model.at(index.row()).playlist_id)
                                                     )

    def __layout_ui(self):
        # Set up horizontal list
        self.__horizontal_list.setFlow(QListView.LeftToRight)
        self.__horizontal_list.setMinimumHeight(235)
        self.__horizontal_list.setSpacing(20)
        self.__layout_manager.addWidget(self.__horizontal_list)

    def model(self) -> PlaylistModel:
        return self.__model
