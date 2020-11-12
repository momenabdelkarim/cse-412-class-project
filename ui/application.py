"""
This module defines the UI and lays out the QApplication's main window
"""

import sys

from PyQt5.QtCore import QSize, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.helper_functions import get_center_pos
from ui.widgets.main_frame import MainFrame

WINDOW_TITLE = "CSE 412 Team Project"


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
