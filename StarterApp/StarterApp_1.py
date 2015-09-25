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

This customization adds a centering method.
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

    def CenterMethod(self):
        BoundingRectangle = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        BoundingRectangle.moveCenter(centerPoint)
        self.move(BoundingRectangle.topLeft())

if __name__ == '__main__':
    PySideStarterApp = QtGui.QApplication(sys.argv)
    mainWindow = PySideTutorialWindow()
    mainWindow.CenterMethod()
    mainWindow.show()
    PySideStarterApp.exec_()
    sys.exit()
