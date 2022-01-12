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
#     spack install sz3
#
# You can edit this file again by typing:
#
#     spack edit sz3
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Sz3(CMakePackage):
    """SZ3 is the next generation of the SZ compressor framework"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = ""
    url      = "https://github.com/szcompressor/SZ3_Private"
    git      = "git@github.com:szcompressor/SZ3_Private"

    maintainers = ['disheng222']

    version('interp', branch="interp")

    depends_on('zstd')
    depends_on('gsl')
    depends_on('pkgconfig')

    def cmake_args(self):
        return [
            "-DSZ3_USE_BUNDLED_ZSTD=OFF"
            "-DSZ3_DEBUG_TIMINGS=OFF"
            "-DBUILD_SHARED_LIBS=OFF"
        ]
