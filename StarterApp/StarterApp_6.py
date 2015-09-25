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

Here we have added our application Layout and widgets to that layout
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
        self.buildButtons()
        self.setCentralWidget(self.ContainerWidget)

    def CenterMethod(self):
        BoundingRectangle = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        BoundingRectangle.moveCenter(centerPoint)
        self.move(BoundingRectangle.topLeft())

    def buildMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.newAction = QtGui.QAction("&New", self,
                                       shortcut=QtGui.QKeySequence.New,
                                       triggered=self.newFile)
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

    def newFile(self):
        x = 2 + 2
        print(x)

    def buildButtons(self):
        self.ContainerWidget = QtGui.QWidget()
        self.GridLayout = QtGui.QGridLayout(self)
        self.thisButton = QtGui.QPushButton("this", self)
        self.thatButton = QtGui.QPushButton("that", self)
        self.anotherButton = QtGui.QRadioButton("another")
        self.specialSlider = QtGui.QSlider()
        self.specialSlider.setTickInterval(10)
        self.specialSlider.TicksRight
        self.anotherButton.setChecked(True)
        self.GridLayout.addWidget(self.thisButton, 0, 0)
        self.GridLayout.addWidget(self.thatButton, 0, 1)
        self.GridLayout.addWidget(self.anotherButton, 1, 0)
        self.GridLayout.addWidget(self.specialSlider, 2, 3)
        self.ContainerWidget.setLayout(self.GridLayout)

if __name__ == '__main__':
    PySideStarterApp = QtGui.QApplication(sys.argv)
    mainWindow = PySideTutorialWindow()
    mainWindow.buildMenus()
    mainWindow.CenterMethod()
    mainWindow.show()
    PySideStarterApp.exec_()
    sys.exit()
