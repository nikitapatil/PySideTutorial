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
"""

# Standard imports
import sys
from PySide import QtGui  # The System we are using

# Create your Qt Application Object
app = QtGui.QApplication(sys.argv)

# We need a Widget/visual component to go within our application
widget = QtGui.QWidget()
widget.setWindowTitle('Hello World')
widget.show()
app.exec_()

sys.exit()
