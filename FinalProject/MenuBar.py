#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Solutions <www.coroware.com>
#
# Distributed under terms of the MIT license.

"""
This is the menubar for the Final Project for the PySide Tutorial
"""

from PySide import QtGui
i

class MainMenuBar(QtGui.QMenuBar):
    def __init__(self):
        QtGui.QMainBar.__init__(self)
        self.CreateMenus()
        self.fileMenuActions()

    def CreateMenus(self):
        self.fileMenu = self.addMenu("&File")
        self.editMenu = self.addMenu("&Edit")
        self.menuOption1 = self.addMenu("Option 1")
        self.menuOption2 = self.addMenu("Option 2")
        self.helpMenu = self.addMenu("&Help")

    def fileMenuActions(self):
        self.newAction = QtGui.QAction("&New", self,
                                       statusTip="Create a New File",
                                       shortcut= QtGui.QKeySequence.New,
                                       triggered = self.newFile)
        self.openAction = QtGui.QAction("&Open")


