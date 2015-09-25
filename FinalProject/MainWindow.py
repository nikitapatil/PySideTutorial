#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Solutions <www.coroware.com>
# Prepared by: Cameron Owens
# Distributed under terms of the MIT license.

"""
This is the main window Module that we will be using to build our final project.

This main window will call and import other widgets that we will build
"""

# Standard Imports
import sys
from PySide import QtGui


class MainUserWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("PySide Final Project")
        self.setWindowGeometry(1080, 500, 1080, 500)
        self.setMinimumHeight(500)
        self.setMinimumWidth(1080)
        self.AppIcon = QtGui.QIcon('MyAppIcon.png')
        self.setWindowIcon(self.AppIcon)

    def Centermethod(self):
        boundingBox = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        boundingBox.moveCenter(centerPoint)
        self.move(boundingBox.topLeft())

    def CreateStatusBar(self):
        self.statusbar = QtGui.QStatusBar()
        self.statusbar.showMessage("This is a tutorial app", 3000)
        self.setStatusBar(self.statusbar)

    def something(self):
        pass
