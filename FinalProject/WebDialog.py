#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""

"""

from PySide import QtGui, QtWebKit
from PySide.QtCore import QUrl
from PySide QtWebKit import QWebSettings

class WebDialog(QtGui.QDialog):
    def __init__(self, parent, Title="WebDialog",
                 destinationURL="http://www.pytexas.org")
