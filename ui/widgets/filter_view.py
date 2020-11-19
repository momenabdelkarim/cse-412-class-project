"""
This file will define a MediaDetailView.
"""
from typing import Optional

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QComboBox
from backend.handlers import cursor, get_all_available_genres
from ui.helper_functions import get_center_pos


class FilterView(QFrame):
    """
    A FilterView allows the user to apply a genre or rating filter to the media list.
    """

    # Signals
    should_update_media_list = pyqtSignal(str, float)  # Update media list given genre and rating

    def __init__(self, parent_window: QWidget):
        super().__init__(parent_window)  # Create as a standalone window

        self.setFixedWidth(500)
        self.setFixedHeight(300)

        self.__rating_selection = QComboBox(self)
        self.__genre_selection = QComboBox(self)
        self.__search_button = QPushButton("SEARCH", self)
        self.setWindowFlag(Qt.Window)

        self.__layout_manager = QVBoxLayout(self)
        self.__layout_ui()

        # Connect signals to slots
        self.__search_button.clicked.connect(self.__search_clicked)

    def __layout_ui(self):
        """
        Positions a FilterView's sub-widgets on screen
        """
        self.parentWidget().hide()

        # FilterView setup
        self.setGeometry(0, 0, self.parentWidget().width(), self.parentWidget().height())
        self.setObjectName("filter-view")
        self.setWindowTitle("Search")

        self.display_filters()

    def closeEvent(self, close_event):
        self.parentWidget().show()
        super().closeEvent(close_event)

    def display_filters(self):
        layout_combo_manager = QVBoxLayout()

        # Get list of available genres
        available_genres = get_all_available_genres(cursor)
        # Add items to genre combo box
        self.__genre_selection.addItem("---")
        self.__genre_selection.addItems(available_genres)

        # Make list of possible rating selections
        available_ratings = ["0+", "1+", "2+", "3+", "4+", "5+", "6+", "7+", "8+", "9+"]
        # Add items to rating combo box
        self.__rating_selection.addItems(available_ratings)

        layout_combo_manager.addWidget(self.__genre_selection)
        layout_combo_manager.addWidget(self.__rating_selection)
        self.__layout_manager.addLayout(layout_combo_manager)

        # Display cancel button
        layout_button_manager = QHBoxLayout()

        cancel_button = QPushButton("Cancel")
        cancel_button.setObjectName("cancel")

        # Display search button
        layout_button_manager.addWidget(cancel_button, 0, Qt.AlignHCenter)
        layout_button_manager.addWidget(self.__search_button, 0, Qt.AlignHCenter)
        self.__layout_manager.addLayout(layout_button_manager)
        cancel_button.clicked.connect(self.__cancel_clicked)

    @QtCore.pyqtSlot()
    def __cancel_clicked(self):
        """
        Slot that connects to the clicked signal
        Should update media list given genre and rating filters
        """
        self.close()

    @QtCore.pyqtSlot()
    def __search_clicked(self):
        """
        Slot that connects to the clicked signal
        Should update media list given genre and rating filters
        """
        rating_dict = {"0+": 0.0,
                       "1+": 1.0,
                       "2+": 2.0,
                       "3+": 3.0,
                       "4+": 4.0,
                       "5+": 5.0,
                       "6+": 6.0,
                       "7+": 7.0,
                       "8+": 8.0,
                       "9+": 9.0}

        self.should_update_media_list.emit(self.__genre_selection.currentText(),
                                           rating_dict[self.__rating_selection.currentText()])
        self.close()
