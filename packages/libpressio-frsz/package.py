# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class LibpressioFrsz(CMakePackage):
    """Fized Rate SZ"""

    homepage = "https://github.com/robertu94/frsz"
    url = "https://github.com/robertu94/frsz/archive/refs/tags/0.0.2.tar.gz"
    git      = "ssh://git@github.com/robertu94/frsz"

    maintainers = ['robertu94']

    version('master', branch='main')
    version('0.0.3')
    version('0.0.2')
    version('0.0.1')

    depends_on('libpressio@0.89.0:', when="@0.0.2:")
    depends_on('libpressio', when="@0.0.1")

    def cmake_args(self):
        args = [
            "-DBUILD_TESTING=OFF"
        ]
        return args
