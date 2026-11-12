# Copyright 2023-2026 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

try:
    import PySide6
except ModuleNotFoundError as error:
    if error.name != "PySide6":
        raise
    from PyQt5 import QtChart, QtCore, QtGui, QtWidgets

    QAction = QtWidgets.QAction
    QShortcut = QtWidgets.QShortcut
    Signal = QtCore.pyqtSignal
else:
    from PySide6 import QtCharts as QtChart
    from PySide6 import QtCore, QtGui, QtWidgets

    QAction = QtGui.QAction
    QShortcut = QtGui.QShortcut
    Signal = QtCore.Signal
