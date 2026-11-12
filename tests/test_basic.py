# Copyright 2023-2026 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import, division, print_function

import render_profile_viewer


def test_runtime_imports():
    from render_profile_viewer import mainwindow, qt

    assert issubclass(
        mainwindow.RenderProfileChartView,
        qt.QtChart.QChartView,
    )
    assert qt.QAction
    assert qt.QShortcut
    assert qt.QtWidgets.QMenu.exec


def test_qt5_enum_compatibility():
    from render_profile_viewer import qt

    assert qt.QtCore.Qt.Key_Up
    assert qt.QtCore.Qt.AlignBottom
    assert qt.QtCore.Qt.AlignLeft
    assert qt.QtCore.Qt.LeftButton
    assert qt.QtGui.QImage.Format_RGB888
    assert qt.QtChart.QChart.ChartThemeDark
    assert qt.QtWidgets.QFileDialog.Directory
