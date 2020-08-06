# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install dlib
#
# You can edit this file again by typing:
#
#     spack edit dlib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Dlib(CMakePackage):
    """toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://dlib.net/"
    url      = "https://github.com/davisking/dlib/archive/v19.19.tar.gz"

    version('19.19', sha256='7af455bb422d3ae5ef369c51ee64e98fa68c39435b0fa23be2e5d593a3d45b87')

    variant('shared', default=True, description="build the shared libraries")

    depends_on('zlib')
    depends_on('libpng')
    depends_on('libjpeg')
    depends_on('blas')
    depends_on('lapack')

    def cmake_args(self):
        args = []
        if "+shared" in self.spec:
            args.append("-DBUILD_SHARED_LIBS=ON")
        return args
