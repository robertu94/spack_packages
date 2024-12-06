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
#     spack install py-perftrace
#
# You can edit this file again by typing:
#
#     spack edit py-perftrace
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.packages import *


class PyPerftrace(Package):
    """utility script that provides a ease of use layer over linux `perf` for collecting trace information"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/robertu94/perftrace"
    url      = "https://github.com/robertu94/perftrace/archive/refs/tags/0.1.0.tar.gz"

    maintainers = ['robertu94']

    version('0.1.0', sha256='850491e1e26876dc4daf4d89e23f3210c9d0a3a179b969331d1b602f074df26f')

    depends_on('python@3.8:', type=('build', 'run'))
    depends_on('py-pip', type=('build'))

    def install(self, spec, prefix):
        pip = Executable("pip")
        pip("install", ".", "--prefix={}".format(prefix))

