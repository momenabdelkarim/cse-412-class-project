"""
This class is responsible for making HTTP requests asynchronously to set a QLabel's image
"""

from PyQt5.QtCore import QUrl, qDebug, Qt, pyqtSignal, QObject, QRect
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QImage, QBrush, QWindow
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QSslConfiguration, QSsl


class ImageRequester(QObject):
    image_request_finished = pyqtSignal(str, QPixmap)

    def __init__(self, parent: QObject):
        super().__init__(parent)
        self.__image_diameter = 100

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

        img: QImage = pix.toImage()

        # Crop to square image
        img_size = min(img.width(), img.height())
        square_rect = QRect(
            (img.width() - img_size) / 2,
            (img.height() - img_size) / 2,
            img_size,
            img_size
        )
        img = img.copy(square_rect)

        # Draw image in circular frame
        circular_img = QImage(img_size, img_size, QImage.Format_ARGB32)
        circular_img.fill(Qt.transparent)

        painter = QPainter(circular_img)
        painter.setBrush(QBrush(img))
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setRenderHints(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHints(QPainter.SmoothPixmapTransform, True)

        painter.drawEllipse(0, 0, img_size, img_size)
        painter.end()

        # Convert QImage back to QPixmap and scale to desired size
        pixel_ratio = QWindow().devicePixelRatio()
        pix = QPixmap.fromImage(circular_img)
        pix.setDevicePixelRatio(pixel_ratio)
        pix = pix.scaled(self.__image_diameter, self.__image_diameter, Qt.KeepAspectRatio, Qt.SmoothTransformation)

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
