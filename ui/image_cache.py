"""
Object used to request images via HTTPS and store them for later retrieval
"""
from typing import Dict

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPixmap

from ui.image_requester import ImageRequester


class ImageCache(QObject):
    new_image_resolved = pyqtSignal(str, QPixmap)

    def __init__(self, parent: QObject):
        super().__init__(parent)

        self.__image_cache: Dict[str: QPixmap] = dict()
        self.__requester = ImageRequester(self)

        # Connect signals to slots
        self.__requester.image_request_finished.connect(self.__handle_icon_response)

    def request_url(self, url: str):
        self.__requester.request(url)

    def get_pixmap(self, url: str) -> QPixmap:
        return self.__image_cache.get(url)

    # Slots
    @QtCore.pyqtSlot(str, QPixmap)
    def __handle_icon_response(self, url: str, pix: QPixmap):
        """
        Handles an image request response from ImageRequester
        """
        self.__image_cache[url] = pix
        self.new_image_resolved.emit(url, pix)


_parent = QObject()
image_cache = ImageCache(_parent)
