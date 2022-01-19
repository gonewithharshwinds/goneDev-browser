# Project of goneHarsh
# Author: Harsh Ajay Mehta
# description: "gonewithharshwinds"
# email: gonewithharshwinds@gmail.com
# url: "https://linktr.ee/gonewithharshwinds"
# github_username: gonewithharshwinds

# importing the required libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # browser title
        title = "goneDev Browser"
        self.setWindowTitle(title)
        # window geometry
        screen_resolution = App.desktop().screenGeometry()
        maxX, maxY = screen_resolution.width(), screen_resolution.height()
        self.setGeometry(0,0,maxX,maxY)

        # show all
        self.show()
        # browser setup
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)

        # navigation bar
        gH_nav = QToolBar()
        self.addToolBar(gH_nav)

        # home btn
 #       gH_home = QAction('Home', self)
  #      gH_home.triggered.connect(self.browser.navigate_home)
  #      gH_nav.addAction(gH_home)

        # back btn
        gH_back = QAction('Back', self)
        gH_back.triggered.connect(self.browser.back)
        gH_nav.addAction(gH_back)

        # forward btn
        gH_frwd = QAction('Forward', self)
        gH_frwd.triggered.connect(self.browser.forward)
        gH_nav.addAction(gH_frwd)

        # reload btn
        gH_reload = QAction('Reload', self)
        gH_reload.triggered.connect(self.browser.reload)
        gH_nav.addAction(gH_reload)

        # search bar
        self.gH_url = QLineEdit()
        self.gH_url.returnPressed.connect(self.navigate_to_url)
        gH_nav.addWidget(self.gH_url)
        self.gH_url.resize(180,20)
        self.browser.urlChanged.connect(self.update_url)

    def navigation_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        url = self.gH_url.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, a):
        self.gH_url.setText(a.toString())



# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())
