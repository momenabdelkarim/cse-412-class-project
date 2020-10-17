"""
Collates a collection of MediaViews into one MediaList
"""
from PyQt5.QtCore import QSize, QObject
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QListView

from ui.widgets.delegate.media_delegate import MediaDelegate
from ui.widgets.model.media_list_model import MediaListModel


class MediaListView(QFrame):

    def __init__(self, parent: QObject):
        super().__init__(parent)

        self.__model = MediaListModel(self)
        self.__item_delegate = MediaDelegate(self)

        self.__list_view = QListView(self)
        self.__list_view.setModel(self.__model)
        self.__list_view.setItemDelegate(self.__item_delegate)

        self.__layout_manager = QVBoxLayout(self)
        self.__layout_ui()

    def __layout_ui(self):
        self.__list_view.setSpacing(22)
        self.__layout_manager.addWidget(self.__list_view)

    def model(self) -> MediaListModel:
        return self.__model