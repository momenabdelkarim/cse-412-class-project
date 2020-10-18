"""
This class is responsible for making HTTP requests asynchronously to set a QLabel's image
"""

from PyQt5.QtCore import QUrl, qDebug, Qt, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QPainter, QImage, QBrush, QWindow
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QSslConfiguration, QSsl

from ui.helper_functions import convert_pixmap_to_square_img, scale_pixmap


class ImageRequester(QObject):
    image_request_finished = pyqtSignal(str, QPixmap)

    def __init__(self, parent: QObject):
        super().__init__(parent)

        self.__net_man = QNetworkAccessManager()
        self.__net_man.finished.connect(self.__request_finished)

    def __del__(self):
        del self.__net_man

    def __request_finished(self, reply: QNetworkReply):
        """
        Slot attached to finished signal of network access manager
        Retrieves HTTP data and sets image appropriately
        """

        pix = QPixmap()

        if reply.error() != QNetworkReply.NoError:
            qDebug(f"Unable to fetch image at {reply.url()}")
        else:
            img_data = reply.readAll()
            pix.loadFromData(img_data)
            reply.deleteLater()

        if pix.isNull():
            pix.load(R"img/default_photo.png")

        # Emit signal
        self.image_request_finished.emit(reply.url().toString(), pix)

    def request(self, image_url: str):
        """
        Make HTTP request asynchronously
        """
        request = QNetworkRequest(QUrl(image_url))
        request.setRawHeader(b"User-Agent", b"412 Image Requester")

        # Configure to utilize SSL
        config = QSslConfiguration.defaultConfiguration()
        config.setProtocol(QSsl.TlsV1_2)

        request.setSslConfiguration(config)

        self.__net_man.get(request)
