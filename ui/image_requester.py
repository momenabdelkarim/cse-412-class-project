"""
This class is responsible for making HTTP requests asynchronously to set a QLabel's image
"""
from typing import Optional

from PyQt5.QtCore import QUrl, QObject, qDebug, Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QSslConfiguration, QSsl
from PyQt5.QtWidgets import QLabel


class ImageRequester(QObject):
    def __init__(self, parent: QObject, label: QLabel, image_url: Optional[str]):
        super().__init__(parent)

        self.__label = label
        self.__image_url = image_url
        self.__pix = QPixmap()
        self.__image_radius = 100

        self.__net_man = QNetworkAccessManager(self)
        self.__net_man.finished.connect(self.__request_finished)

    def __request_finished(self, reply: QNetworkReply):
        """
        Slot attached to finished signal of network access manager
        Retrieves HTTP data and sets image appropriately
        """
        print("HERE")
        print(reply.attribute(QNetworkRequest.HttpStatusCodeAttribute))

        if reply.error() != QNetworkReply.NoError:
            qDebug(f"Unable to fetch image at {self.__image_url}")
        else:
            img_data = reply.readAll()
            self.__pix.loadFromData(img_data)
            reply.deleteLater()

        # if self.__pix.isNull():
        #     self.__pix.load(R"img/default_photo.png")

        # Make pixmap scale reasonably
        pix = self.__pix.scaled(self.__image_radius, self.__image_radius, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Add an elliptical radius to the image
        circular_pix = QPixmap(self.__image_radius, self.__image_radius)
        circular_pix.fill(Qt.transparent)

        painter = QPainter(circular_pix)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setRenderHints(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHints(QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.__image_radius, self.__image_radius, self.__image_radius / 2,
                            self.__image_radius / 2)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pix)

        painter.end()

        self.__label.setPixmap(circular_pix)

    def request(self):
        """
        Make HTTP request asynchronously
        """
        request = QNetworkRequest(QUrl(self.__image_url))
        request.setRawHeader(b"User-Agent", b"412 Image Requester")

        # Configure to utilize SSL
        config = QSslConfiguration.defaultConfiguration()
        config.setProtocol(QSsl.TlsV1_2)

        request.setSslConfiguration(config)

        self.__net_man.get(request)
