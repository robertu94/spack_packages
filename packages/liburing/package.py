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
#     spack install liburing
#
# You can edit this file again by typing:
#
#     spack edit liburing
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Liburing(AutotoolsPackage):
    """high level interface for linux io_uring"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/axboe/liburing"
    url      = "https://github.com/axboe/liburing/archive/refs/tags/liburing-2.1.tar.gz"
    git      = homepage

    maintainers = ['robertu94']

    version('2.1', sha256='f1e0500cb3934b0b61c5020c3999a973c9c93b618faff1eba75aadc95bb03e07')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
