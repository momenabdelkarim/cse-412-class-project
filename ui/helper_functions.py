"""
This file contains extraneous functions that are helpful throughout the UI widgets and modules
"""
from typing import List

from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QColor, QImage, QWindow, QPainter, QBrush
from PyQt5.QtWidgets import QWidget, QApplication


def get_center_pos(widget: QWidget) -> QPoint:
    """
    Calculates and returns the center position of the primary screen (including widget size)
    :param widget: Widget to be centered within the primary screen
    :return: A QPoint, pointing to the origin of the screen's adjusted center
    """

    center_screen: QPoint = QApplication.desktop().availableGeometry().center()
    return center_screen - widget.rect().center()


def scale_pixmap(pixmap: QPixmap, width: int, height: int) -> QPixmap:
    """
    Scales the given pixmap to the given width and height
    """
    pixel_ratio = QWindow().devicePixelRatio()
    pixmap.setDevicePixelRatio(pixel_ratio)
    return pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)


def convert_pixmap_to_circular(pixmap: QPixmap, diameter: int) -> QPixmap:
    img: QImage = convert_pixmap_to_square_img(pixmap)
    img_size = img.width()

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
    pix = QPixmap.fromImage(circular_img)
    pix = scale_pixmap(pix, diameter, diameter)

    return pix


def convert_pixmap_to_square_img(pixmap: QPixmap) -> QImage:
    """
    Crops and scales the given pixmap to be a square
    :param pixmap: Pixmap to be scaled
    """

    img: QImage = pixmap.toImage()

    # Crop to square image
    img_size = min(img.width(), img.height())
    square_rect = QRect(
        (img.width() - img_size) / 2,
        (img.height() - img_size) / 2,
        img_size,
        img_size
    )

    return img.copy(square_rect)


def icon_with_color(img_fp: str, color: QColor):
    """
    Changes the given image icon's color to the provided color
    :param img_fp: File path of image to be changed
    :param color: Color to change image to
    :return: None
    """

    pix = QPixmap(img_fp)
    mask = pix.createMaskFromColor(Qt.black, Qt.MaskOutColor)
    pix.fill(color)
    pix.setMask(mask)

    return QIcon(pix)


def tile_pixmaps(pixmaps: List[QPixmap], tile_height: int) -> QPixmap:
    tiled_pix = QPixmap(tile_height, tile_height)
    tiled_pix.fill(Qt.transparent)

    painter = QPainter(tiled_pix)
    painter.setRenderHints(QPainter.Antialiasing, True)
    painter.setRenderHints(QPainter.HighQualityAntialiasing, True)
    painter.setRenderHints(QPainter.SmoothPixmapTransform, True)

    # Convert each pixmap to square and scale down
    for (i, pix) in enumerate(pixmaps[:4]):
        pix = QPixmap.fromImage(convert_pixmap_to_square_img(pix))

        # Scale each to half of tile_height
        pix_diameter = int(tile_height / 2)
        pix = scale_pixmap(pix, pix_diameter, pix_diameter)

        if i == 0:
            # Draw top left
            painter.drawPixmap(0, 0, pix)
        elif i == 1:
            # Draw top right
            painter.drawPixmap(pix_diameter, 0, pix)
        elif i == 2:
            # Draw bottom left
            painter.drawPixmap(0, pix_diameter, pix)
        else:
            # Draw bottom right
            painter.drawPixmap(pix_diameter, pix_diameter, pix)

    painter.end()
    return tiled_pix


def show_child_window(parent_window: QWidget, child_window: QWidget):
    """
    Utility window to show a new child window in the same position as its parent
    :parent_window: Window in the "parent" relationship (that is, to be hidden)
    :child_window: Window in the "child" relationship (that is, to be shown at the same position)
    """
    child_window.move(parent_window.pos())
    child_window.show()


def colorize_pixmap(file_path: str, color: QColor) -> QPixmap:
    """
    Loads an icon, paints it the given color, and builds an icon
    :param file_path: Path where the icon is stored, to be loaded as a pixmap
    :param color: Color to paint pixmap
    :return: a new QIcon containing the photo at file_path
    """

    photo_pixmap = QPixmap(file_path)
    themed_pixmap = QPixmap(photo_pixmap.size())

    themed_pixmap.fill(color)
    themed_pixmap.setMask(photo_pixmap.createMaskFromColor(Qt.transparent))

    return themed_pixmap
