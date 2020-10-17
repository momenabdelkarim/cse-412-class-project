import sys

from PyQt5.QtCore import QSize, QPoint, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTabWidget, QVBoxLayout

from ui.widgets.media_list import MediaListView
from ui.widgets.model.media import Media

WINDOW_TITLE = "CSE 412 Team Project"


def get_center_pos(widget: QWidget) -> QPoint:
    """
    Calculates and returns the center position of the primary screen, accounting for the widget's size
    :param widget: Widget to be centered within the primary screen
    :return: A QPoint, pointing to the origin of the screen's adjusted center
    """

    center_screen: QPoint = QApplication.desktop().availableGeometry().center()
    return center_screen - widget.rect().center()


class Application(QObject):
    """
    Represents entire application, instantiated to create actual User Interface
    """

    def build_debug_media_list(self) -> MediaListView:
        colter_album = Media("Imaginary Appalachia", "Colter Wall",
                             "https://www.outhousetickets.com/Artist/3807/photo/colter-wall-event.png")
        tom_special = Media("Mostly Stories", "Tom Segura",
                            "https://images-na.ssl-images-amazon.com/images/I/71XbjhskX0L._SL1500_.jpg")
        joe_podcast = Media("The Joe Rogan Experience #1169", "Joe Rogan Ft. Elon Musk",
                            "https://i.ytimg.com/vi/ycPr5-27vSI/sddefault.jpg")

        DEBUG_MEDIA_LIST = MediaListView(self.__main_win)
        DEBUG_MEDIA_LIST.model().add_media(colter_album)
        DEBUG_MEDIA_LIST.model().add_media(tom_special)
        DEBUG_MEDIA_LIST.model().add_media(joe_podcast)

        return DEBUG_MEDIA_LIST

    def __init__(self):
        super().__init__(None)

        self.app_dimensions = QSize(700, 800)
        self.__app = QApplication(sys.argv)
        self.__main_win = QMainWindow(parent=None)
        self.__main_win.setWindowTitle("CSE412 Team Project")

        qwidget = QWidget()
        layout = QVBoxLayout(qwidget)

        # Creating tabs
        tabs = QTabWidget()

        # Tab Items
        tab1 = QWidget()
        tab2 = QWidget()

        # Name Tab Items
        tabs.addTab(tab1, "All Media")
        tabs.addTab(tab2, "Playlist")

        tablelayout = QVBoxLayout()
        button1 = QPushButton("Query All Media")
        tablelayout.addWidget(button1)
        tab1.setLayout(tablelayout)

        tablelayout2 = QVBoxLayout()
        button2 = QPushButton("Query Playlist")
        tablelayout2.addWidget(button2)
        tab2.setLayout(tablelayout2)

        layout.addWidget(tabs)
        qwidget.setLayout(layout)

        self.__main_win.setCentralWidget(self.build_debug_media_list())
        self.__generate_window()

    def __generate_window(self):
        """
        Generate's the application and it's primary window.
        """

        with open('ui/style/style.qss', 'r') as file:
            self.__app.setStyleSheet(file.read())

        QApplication.setApplicationDisplayName(WINDOW_TITLE)

        # Move main window to center of center monitor's display area
        self.__main_win.setGeometry(0, 0, self.app_dimensions.height(), self.app_dimensions.width())
        self.__main_win.move(get_center_pos(self.__main_win))
        self.__main_win.show()

        sys.exit(self.__app.exec())
