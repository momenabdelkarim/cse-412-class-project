from PyQt5.QtCore import QSize, QModelIndex, Qt, QRect
from PyQt5.QtGui import QFontMetrics, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QApplication


class MediaDelegate(QStyledItemDelegate):
    """
    Item delegate used for displaying any piece of media with a custom style
    """

    icon_diameter = 100
    pad_horizontal = 10
    pad_vertical = 10
    icon_padding = 20
    total_icon_width = icon_diameter + icon_padding

    def sizeHint(self, option: 'QStyleOptionViewItem', index: QModelIndex) -> QSize:
        if not index.isValid():
            return QSize()

        media = index.model().at(index.row())

        font = QApplication.font()
        msg_fm = QFontMetrics(font)

        media_rect = msg_fm.boundingRect(0, 0, option.rect.width() - MediaDelegate.icon_diameter,
                                         0,
                                         Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, media.title())
        media_size = QSize(option.rect.width(), media_rect.height() + (2 * MediaDelegate.icon_padding))

        if media_size.height() < MediaDelegate.icon_diameter:
            media_size.setHeight(MediaDelegate.icon_diameter)

        return media_size

    def paint(self, painter: QPainter, option: 'QStyleOptionViewItem', index: QModelIndex) -> None:
        """
        Paints the message on the screen

        :param painter: Controls actual painting
        :param option: Options for painting
        :param index: Index of item
        """

        media = index.model().at(index.row())

        if not index.isValid():
            return

        painter.save()  # Save current state, before altering for custom painting

        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setRenderHints(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHints(QPainter.SmoothPixmapTransform, True)

        media_pix: QPixmap = index.data(Qt.DecorationRole)

        title_font = QApplication.font()
        title_font.setPixelSize(22)
        title_fm = QFontMetrics(title_font)

        subtitle_font = QApplication.font()
        subtitle_fm = QFontMetrics(subtitle_font)

        icon_rect = QRect(option.rect.left() + MediaDelegate.pad_horizontal,
                          option.rect.top() + MediaDelegate.pad_vertical,
                          MediaDelegate.icon_diameter,
                          MediaDelegate.icon_diameter)

        title_rect = title_fm.boundingRect(icon_rect.right() + MediaDelegate.icon_padding,
                                           icon_rect.top() + MediaDelegate.pad_vertical + 10,
                                           option.rect.width() - MediaDelegate.total_icon_width,
                                           0,
                                           Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, media.title())

        subtitle_rect = subtitle_fm.boundingRect(icon_rect.right() + MediaDelegate.icon_padding,
                                                 title_rect.bottom() + MediaDelegate.pad_vertical,
                                                 option.rect.width() - MediaDelegate.total_icon_width,
                                                 0,
                                                 Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, media.subtitle())
        # Draw surrounding rect
        bound_rect = QRect(MediaDelegate.pad_horizontal,
                           icon_rect.top() - MediaDelegate.pad_vertical,
                           option.rect.width(),
                           icon_rect.height() + (2 * MediaDelegate.pad_horizontal))
        bound_color = QColor(31, 31, 31)

        # Paint background
        painter.setBrush(bound_color)
        painter.setPen(bound_color)
        painter.drawRoundedRect(bound_rect, 5, 5)

        # Paint icon
        painter.drawPixmap(icon_rect, media_pix)

        # Paint title
        painter.setFont(title_font)
        painter.setPen(Qt.white)
        painter.drawText(title_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, media.title())

        # Paint subtitle
        painter.setFont(subtitle_font)
        painter.setPen(QColor(195, 195, 195))
        painter.drawText(subtitle_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, media.subtitle())
        painter.restore()
