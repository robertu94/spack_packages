# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Tif22pnm(Package):
    """tif22pnm: TIFF-to-PNM converter and png22pnm, a PNG-to-PNM converter"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/pts/tif22pnm"
    url      = "https://github.com/pts/tif22pnm/archive/2014-01-09.tar.gz"
    git      = homepage

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master', branch="master")

    # FIXME: Add dependencies if required.
    depends_on('libpng')
    depends_on('libtiff')

    def install(self, spec, prefix):
        configure_args = [
            "--prefix=" + prefix
        ]
        configure(*configure_args)
        do_script =  Executable("./do.sh")
        do_script("fast", spec['libpng'].prefix)
        mkdirp(prefix.bin)
        install("./tif22pnm", prefix.bin)
