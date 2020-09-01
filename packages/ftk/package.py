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
#     spack install ftk
#
# You can edit this file again by typing:
#
#     spack edit ftk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ftk(CMakePackage):
    """Feature Tracking Toolkit"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/hguo/ftk"
    url      = "https://github.com/hguo/ftk/archive/0.0.2.tar.gz"
    git      = "https://github.com/hguo/ftk.git"

    # FIXME: Add proper versions here.
    version("master", branch="master")
    version("dev", branch="dev")
    version('0.0.2.2', sha256='e699637a7ebca5e776a56dd8ccb6a00a024909f79d084be087613c3ccaf42e7d')
    version('0.0.2.1', sha256='cb593334c7029b3b639a0d4e7e9dcbd471045c6c32344c5fc856626c8d5d506b')
    version('0.0.2',   sha256='1ab7d84c1b937375b614eb7f3332648422e6371e71905c954611188505db3ead')


    variant("vtk", default=False)

    # FIXME: Add dependencies if required.
    depends_on('cmake@3.10:', type="build")
    depends_on('hdf5')
    depends_on('mpi')
    depends_on('netcdf-c')
    depends_on('vtk', when="+vtk")

    def cmake_args(self):

        return [
            "-DFTK_USE_MPI=ON"
        ]
