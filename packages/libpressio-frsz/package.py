# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class LibpressioFrsz(CMakePackage):
    """Fized Rate SZ"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/robertu94/frsz"
    url = "https://github.com/robertu94/frsz"
    git      = "ssh://git@github.com/robertu94/frsz"

    maintainers = ['robertu94']

    version('master', branch='main')

    depends_on('libpressio')

    def cmake_args(self):
        args = [
            "-DBUILD_TESTING=OFF"
        ]
        return args
