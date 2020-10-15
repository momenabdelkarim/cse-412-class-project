"""
This file contains extraneous functions that are helpful throughout the UI widgets and modules
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QColor


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
