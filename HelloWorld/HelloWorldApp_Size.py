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
This is the first Application to be written using PySide

Here we have added the size option of the central widget and have
added a window title.
"""

# Standard imports
import sys
from PySide import QtGui  # The System we are using

# Create your Qt Application Object
firstApp = QtGui.QApplication(sys.argv)

# We need a Widget/visual component to go within our application
widget = QtGui.QWidget()
widget.resize(500, 250)
widget.setWindowTitle('Hello World')
widget.show()
firstApp.exec_()

sys.exit()
