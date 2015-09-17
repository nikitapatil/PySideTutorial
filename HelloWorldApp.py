#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cowens@coroware.com>
# Twitter: Candid Cypher
# Git: CandidCypher
#
# Distributed under terms of the MIT license.

"""
This is the first application people writing PySide Apps get started with;
Hello World
"""

import sys
from PySide.QtCore import *
from PySide.QtGui import *


# Create your Qt Application Object
app = QApplication(sys.argv)

label = QLabel("Hello World")
label.show()

app.exec_()
sys.exit()
