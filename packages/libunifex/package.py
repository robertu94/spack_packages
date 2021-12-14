# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install libunifex
#
# You can edit this file again by typing:
#
#     spack edit libunifex
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Libunifex(CMakePackage):
    """Unified Executors Implementation"""

    homepage = "https://github.com/facebookexperimental/libunifex"
    git      = "https://github.com/facebookexperimental/libunifex"

    # FIXME: Add proper versions and checksums here.
    version('main', branch='main')

    # FIXME: Add dependencies if required.
    depends_on('liburing')

    def cmake_args(self):
        args = [
            "-DBUILD_TESTING=OFF",
            "-DBUILD_TESTING=OFF",
            "-DUNIFEX_BUILD_EXAMPLES=OFF"
        ]
        return args
