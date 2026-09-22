# Copyright 2023-2026 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required (VERSION 3.23.1)

include(OMR_PackageVersion)  # Sets versionString, projectString and PACKAGE_NAME
project(${projectString}
    VERSION ${versionString}
    LANGUAGES NONE) # don't try to test the CXX compiler

find_package(Python REQUIRED COMPONENTS Interpreter)

set(pythonInstallDir
    python/lib/python${Python_VERSION_MAJOR}.${Python_VERSION_MINOR})

install(DIRECTORY render_profile_viewer
        DESTINATION ${pythonInstallDir}
        PATTERN "__pycache__" EXCLUDE
        PATTERN "*.pyc" EXCLUDE)

install(PROGRAMS bin/render_profile_viewer
        DESTINATION bin)
