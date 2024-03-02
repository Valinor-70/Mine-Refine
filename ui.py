# ui.py
from PySide6.QtCore import QRect, QMetaObject, QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMenuBar, QInputDialog, \
    QTabWidget, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QTextEdit, QStatusBar
from PySide6.QtGui import QAction


def apply_dark_theme(app):
    app.setStyleSheet("""
        /* Set the background color of all widgets to dark-gray */
        QWidget {
            background-color: #2b2b2b;
            color: #b1b1b1;
            border: 1px solid #3e3e3e;
        }

        /* Set the background color of all buttons to dark-gray */
        QPushButton {
            background-color: #353535;
            border: 1px solid #4e4e4e;
            padding: 5px;
        }

        /* Set the background color of all buttons when hovered to gray */
        QPushButton:hover {
            background-color: #3e3e3e;
        }

        /* Set the background color of all buttons when pressed to light-gray */
        QPushButton:pressed {
            background-color: #4e4e4e;
        }

        /* Set the background color of the tab widget to dark-gray */
        QTabWidget {
            background-color: #2b2b2b;
            color: #b1b1b1;
            border: 1px solid #3e3e3e;
        }

        /* Set the background color of the tab bar to dark-gray */
        QTabBar {
            background-color: #2b2b2b;
            color: #b1b1b1;
            border: 1px solid #3e3e3e;
        }

        /* Set the background color of the tab to dark-gray */
        QTab {
            background-color: #2b2b2b;
            color: #b1b1b1;
            border: 1px solid #3e3e3e;
        }

        /* Set the background color of the text edit to dark-gray */
        QTextEdit {
            background-color: #2b2b2b;
            color: #b1b1b1;
            border: 1px solid #3e3e3e;
        }

        /* Set the background color of the status bar to dark-gray */
        QStatusBar {
            background-color: #2b2b2b;
            color: #b1b1b1;
            border: 1px solid #3e3e3e;
        }
    """)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QTextEdit(self.tab)
        self.text.setObjectName("text")
        self.verticalLayout_2.addWidget(self.text)
        self.mine_button = QPushButton(self.tab)
        self.mine_button.setObjectName("mine_button")
        self.verticalLayout_2.addWidget(self.mine_button)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.start_new_game_button = QPushButton(self.tab_2)
        self.start_new_game_button.setObjectName("start_new_game_button")
        self.verticalLayout_3.addWidget(self.start_new_game_button)
        self.load_existing_game_button = QPushButton(self.tab_2)
        self.load_existing_game_button.setObjectName("load_existing_game_button")
        self.verticalLayout_3.addWidget(self.load_existing_game_button)
        self.leaderboard_button = QPushButton(self.tab_2)
        self.leaderboard_button.setObjectName("leaderboard_button")
        self.verticalLayout_3.addWidget(self.leaderboard_button)
        self.exit_button = QPushButton(self.tab_2)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_3.addWidget(self.exit_button)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mine_button.setText(_translate("MainWindow", "Mine"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mine"))
        self.start_new_game_button.setText(_translate("MainWindow", "Start New Game"))
        self.load_existing_game_button.setText(_translate("MainWindow", "Load Existing Game"))
        self.leaderboard_button.setText(_translate("MainWindow", "Leaderboard"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Menu"))
