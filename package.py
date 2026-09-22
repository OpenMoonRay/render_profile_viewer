# Copyright 2023-2026 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

import sys

uuid = "73528efd-c17e-40b7-aaf0-6b4e31358c55"
name = "render_profile_viewer"  # This must match the value in setup.cfg.
requires_rez_version = "2"
help = "http://readthedocs/docs/render_profile_viewer/en/stable"

authors = [
    'moonbase-dev@dreamworks.com',
]

# Supply arguments to the "python setup.py" call rez-build will make.
# These are appended after "python setup.py build [install]"
# Add --no-build-sphinx to disable the automatic building of docs.
# Keep these keys aligned with the Python classifiers in setup.cfg.
rez_build_args = {
    'python-3.10': ['--no-build-sphinx'],
    'python-3.11': ['--no-build-sphinx'],
    'python-3.13': ['--no-build-sphinx'],
}

if 'cmake' in sys.argv:
    build_system = 'cmake'
    private_build_requires = [
        'cmake_modules-2.0'
    ]
else:
    build_system = 'setuptools'

def preprocess(this, data):
    from rez.package_py_utils import InvalidPackageError
    from rez.utils.formatting import PackageRequest
    try:
        import rezbuild.earlybind
    except ImportError:
        raise InvalidPackageError("The package cannot be configured because "
                                  "rezbuild.earlybind cannot be imported.")
    rezbuild.earlybind.configure_package(this, data)

    variant_dependencies = {
        "python-3.10": [
            "PyQt5-5.15.6+<5.15.6.1",
            "PyQtChart-5.15.6+<5.15.6.1",
            "openimageio-2.3.20+<2.3.20.1",
            "numpy-1.26+<2",
        ],
        "python-3.11": [
            "PySide6-6.5.5+<6.6",
            "openimageio-3.0+<3.1",
            "numpy-1.26+<2",
        ],
        "python-3.13": [
            "PySide6-6.8.6+<6.9",
            "openimageio-3.1+<3.2",
            "numpy-2.3+<2.4",
        ],
    }
    conditional_families = {
        PackageRequest(requirement).name
        for requirements in variant_dependencies.values()
        for requirement in requirements
    }
    data["requires"] = [
        requirement
        for requirement in data["requires"]
        if PackageRequest(str(requirement)).name not in conditional_families
    ]
    for variant in data["variants"]:
        python_requirement = next(
            str(requirement)
            for requirement in variant
            if PackageRequest(str(requirement)).name == "python"
        )
        variant.extend(variant_dependencies[python_requirement])


@late()
def test_arguments():
    import os
    return os.getenv("REZ_TEST_ARGUMENTS", "")


def commands():
    env.PYTHONPATH.append("{root}")
    env.PYTHONPATH.append("{root}/python/lib/$PYTHON_NAME")
    env.PATH.append("{root}/bin")
    env.RPV_ANNOTATIONS_DIR = "/work/gshad/moonshine/render_profile_viewer"
    env.RPV_PROFILE_DIR = "/work/rd/raas/moonray/ProfileRuns/latest_results/profile_reports"

with scope("config") as config:
    config.package_filter = []
