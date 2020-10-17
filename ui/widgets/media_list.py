"""
Collates a collection of MediaViews into one MediaList
"""
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, QObject, QModelIndex
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QListView, QDialog

from ui.widgets.delegate.media_delegate import MediaDelegate
from ui.widgets.dialogs import AddToPlaylistDialog
from ui.widgets.model.media_list_model import MediaListModel


class MediaListView(QFrame):

    def __init__(self, parent: QObject):
        super().__init__(parent)

        self._model = MediaListModel(self)
        self._item_delegate = MediaDelegate(self)

        self._list_view = QListView(self)
        self._list_view.setModel(self._model)
        self._list_view.setItemDelegate(self._item_delegate)

        self._layout_manager = QVBoxLayout(self)
        self._layout_ui()

    def _layout_ui(self):
        self._list_view.setSpacing(22)
        self._layout_manager.addWidget(self._list_view)

    def model(self) -> MediaListModel:
        return self._model


class AddMediaListView(MediaListView):
    def __init__(self, parent: QObject):
        super().__init__(parent)

        # Connect signals to slots
        self._list_view.doubleClicked.connect(self.__item_double_clicked)

    @QtCore.pyqtSlot(QModelIndex)
    def __item_double_clicked(self, index: QModelIndex):
        """
        Slot that responds to a user double clicking on any row in the list
        :index: Index of item selected
        """
        print("Here")
        media = self._model.at(index.row())

        if add_dialog := AddToPlaylistDialog(self, media):
            if add_dialog.exec() == QDialog.Accepted:  # Has successfully selected a playlist to add the song to
                # Get selected playlist from dialog and save media to DB
                print(f"ACCEPTED {add_dialog.get_selection()}")