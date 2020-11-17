from PyQt5.QtCore import QSize, QModelIndex, Qt, QRect
from PyQt5.QtGui import QFontMetrics, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QApplication


class ItemDelegate(QStyledItemDelegate):
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

        item = index.model().at(index.row())

        font = QApplication.font()
        msg_fm = QFontMetrics(font)

        item_rect = msg_fm.boundingRect(0, 0, option.rect.width() - ItemDelegate.icon_diameter,
                                        0,
                                        Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, item.name)
        item_size = QSize(option.rect.width(), item_rect.height() + (2 * ItemDelegate.icon_padding))

        if item_size.height() < ItemDelegate.icon_diameter:
            item_size.setHeight(ItemDelegate.icon_diameter)

        return item_size

    def paint(self, painter: QPainter, option: 'QStyleOptionViewItem', index: QModelIndex) -> None:
        """
        Paints the message on the screen

        :param painter: Controls actual painting
        :param option: Options for painting
        :param index: Index of item
        """

        item = index.model().at(index.row())

        if not index.isValid():
            return

        painter.save()  # Save current state, before altering for custom painting

        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setRenderHints(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHints(QPainter.SmoothPixmapTransform, True)

        if index.model().displays_image:
            media_pix: QPixmap = index.data(Qt.DecorationRole)

        title_font = QApplication.font()
        title_font.setPixelSize(22)
        title_fm = QFontMetrics(title_font)

        subtitle_font = QApplication.font()
        subtitle_fm = QFontMetrics(subtitle_font)

        icon_rect = QRect(option.rect.left() + ItemDelegate.pad_horizontal,
                          option.rect.top() + ItemDelegate.pad_vertical,
                          ItemDelegate.icon_diameter,
                          ItemDelegate.icon_diameter)

        title_rect = title_fm.boundingRect(icon_rect.right() + ItemDelegate.icon_padding,
                                           icon_rect.top() + ItemDelegate.pad_vertical + 10,
                                           option.rect.width() - ItemDelegate.total_icon_width,
                                           0,
                                           Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, item.name)

        subtitle_rect = subtitle_fm.boundingRect(icon_rect.right() + ItemDelegate.icon_padding,
                                                 title_rect.bottom() + ItemDelegate.pad_vertical,
                                                 option.rect.width() - ItemDelegate.total_icon_width,
                                                 0,
                                                 Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, item.genre)
        # Draw surrounding rect
        bound_rect = QRect(ItemDelegate.pad_horizontal,
                           icon_rect.top() - ItemDelegate.pad_vertical,
                           option.rect.width(),
                           icon_rect.height() + (2 * ItemDelegate.pad_horizontal))
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
        painter.drawText(title_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, item.name)

        # Paint subtitle
        painter.setFont(subtitle_font)
        painter.setPen(QColor(195, 195, 195))
        painter.drawText(subtitle_rect, Qt.AlignLeft | Qt.AlignTop | Qt.TextWordWrap, item.genre)
        painter.restore()
