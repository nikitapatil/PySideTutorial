#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Solutions <www.coroware.com>
# Prepared by: Cameron Owens
# Twitter: Candid Cypher
# Git: CandidCypher
#
# Distributed under terms of the MIT license.

"""
Here we start customizing our application.

In this version we will add menu bars for more interction.
"""

# Standard imports
import sys
from PySide import QtGui  # The System we are using


# Here we have changed to a much more OOP design
class PySideTutorialWindow(QtGui.QMainWindow):
    '''
    This is our main container widget that we will put everything into
    '''
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("PySide Tutorial App")
        self.setGeometry(1080, 500, 1080, 500)
        self.setMinimumHeight(500)
        self.setMinimumWidth(200)
        PySideAppIcon = QtGui.QIcon('MyAppIcon.png')
        self.setWindowIcon(PySideAppIcon)

    def CenterMethod(self):
        BoundingRectangle = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        BoundingRectangle.moveCenter(centerPoint)
        self.move(BoundingRectangle.topLeft())

    def buildMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.newAction = QtGui.QAction("&New", self,
                                       shortcut=QtGui.QKeySequence.New)
        self.fileMenu.addAction(self.newAction)
        self.openAction = QtGui.QAction("&Open", self,
                                        shortcut=QtGui.QKeySequence.Open)
        self.fileMenu.addAction(self.openAction)
        self.saveAction = QtGui.QAction("&Save", self,
                                        shortcut=QtGui.QKeySequence.Save)
        self.fileMenu.addAction(self.saveAction)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.transformAction = QtGui.QAction("&Transform", self, shortcut=QtGui.QKeySequence("Ctrl+T"))
        self.editMenu.addAction(self.transformAction)
        self.helpMenu = self.menuBar().addMenu("&Help")

if __name__ == '__main__':
    PySideStarterApp = QtGui.QApplication(sys.argv)
    mainWindow = PySideTutorialWindow()
    mainWindow.buildMenus()
    mainWindow.CenterMethod()
    mainWindow.show()
    PySideStarterApp.exec_()
    sys.exit()
