# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install libpressio-adios2
#
# You can edit this file again by typing:
#
#     spack edit libpressio-adios2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class LibpressioAdios2(CMakePackage):
    """An IO plugin to read/write ADIOS2 files for LibPressio"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/robertu94/libpressio_adios2"
    url      = "https://github.com/robertu94/libpressio_adios2/archive/refs/tags/0.0.1.tar.gz"

    maintainers = ['robertu94']

    version('0.0.1', sha256='ab9c7e26114e8d81f8ad8aca703855079cd3441f9b72e01d9b4aeb0c57ce0746')

    depends_on('libpressio@0.60.0:+mpi')
    depends_on('adios2@2.8.0:+mpi')

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("LIBPRESSIO_ADIOS2_WERROR", False)
        ]
        return args