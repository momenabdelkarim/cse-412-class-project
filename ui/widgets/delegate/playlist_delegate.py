from PyQt5.QtCore import QModelIndex, QSize, Qt, QRect
from PyQt5.QtGui import QFontMetrics, QPainter, QPixmap
from PyQt5.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QApplication


class PlaylistDelegate(QStyledItemDelegate):
    """
    Item delegate used for displaying a playlist with a custom style
    """

    icon_diameter = 150
    pad_horizontal = 10
    pad_vertical = 10
    icon_padding = 20
    total_icon_width = icon_diameter + icon_padding + (2 * pad_horizontal)

    def sizeHint(self, option: 'QStyleOptionViewItem', index: QModelIndex) -> QSize:
        if not index.isValid():
            return QSize()

        playlist = index.model().at(index.row())

        font = QApplication.font()
        title_fm = QFontMetrics(font)

        playlist_rec = title_fm.boundingRect(0, 0, option.rect.width() - PlaylistDelegate.icon_diameter,
                                             0,
                                             Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, playlist.name)
        title_rect = title_fm.boundingRect(option.rect.left() + PlaylistDelegate.pad_horizontal,
                                           playlist_rec.bottom() + PlaylistDelegate.pad_vertical,
                                           playlist_rec.width(),
                                           0,
                                           Qt.AlignHCenter | Qt.AlignTop | Qt.TextWordWrap,
                                           playlist.name)

        playlist_size = QSize(PlaylistDelegate.icon_diameter, playlist_rec.height() + PlaylistDelegate.pad_vertical + title_rect.height())

        if playlist_size.height() < PlaylistDelegate.icon_diameter:
            playlist_size.setHeight(PlaylistDelegate.icon_diameter)

        return playlist_size

    def paint(self, painter: QPainter, option: 'QStyleOptionViewItem', index: QModelIndex) -> None:
        """
        Paint the playlist on the screen

        :param painter: Controls actual painting
        :param option: Options for painting
        :param index: Index of item
        """

        playlist = index.model().at(index.row())

        if not index.isValid():
            return

        painter.save()  # Save current state, before altering for custom painting

        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setRenderHints(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHints(QPainter.SmoothPixmapTransform, True)

        playlist_pix: QPixmap = index.data(Qt.DecorationRole)  # Tiled pixmap

        title_font = QApplication.font()
        title_font.setPixelSize(15)
        title_fm = QFontMetrics(title_font)

        icon_rect = QRect(option.rect.left() + PlaylistDelegate.pad_horizontal,
                          option.rect.top(),
                          PlaylistDelegate.icon_diameter,
                          PlaylistDelegate.icon_diameter)

        title_rect = title_fm.boundingRect(option.rect.left() + PlaylistDelegate.pad_horizontal,
                                           icon_rect.bottom() + PlaylistDelegate.pad_vertical,
                                           icon_rect.width(),
                                           0,
                                           Qt.AlignHCenter | Qt.AlignTop | Qt.TextWordWrap,
                                           playlist.name)

        # Draw icon
        painter.drawPixmap(icon_rect, playlist_pix)

        # Draw title
        painter.setFont(title_font)
        painter.setPen(Qt.white)
        painter.drawText(title_rect, Qt.AlignHCenter | Qt.AlignTop | Qt.TextWordWrap, playlist.name)

        painter.restore()
