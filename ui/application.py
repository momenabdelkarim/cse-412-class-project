"""
This module defines the UI and lays out the QApplication's main window
"""

import sys

from PyQt5.QtCore import QSize, QPoint, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from ui.widgets.main_frame import MainFrame

WINDOW_TITLE = "CSE 412 Team Project"


def get_center_pos(widget: QWidget) -> QPoint:
    """
    Calculates and returns the center position of the primary screen (including widget size)
    :param widget: Widget to be centered within the primary screen
    :return: A QPoint, pointing to the origin of the screen's adjusted center
    """

    center_screen: QPoint = QApplication.desktop().availableGeometry().center()
    return center_screen - widget.rect().center()


class Application(QObject):
    """
    Represents entire application, instantiated to create actual User Interface
    """

    def __init__(self):
        super().__init__(None)

        self.app_dimensions = QSize(700, 800)
        self.__app = QApplication(sys.argv)
        self.__main_win = QMainWindow(parent=None)

        self.__main_win.setCentralWidget(MainFrame(self.__main_win))
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
