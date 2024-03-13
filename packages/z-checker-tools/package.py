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
#     spack install zchecker-tools
#
# You can edit this file again by typing:
#
#     spack edit zchecker-tools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class ZCheckerTools(CMakePackage):
    """A collection of analysis tools that build upon z-checker"""

    homepage = "https://github.com/CODARcode/z-checker-installer"
    url      = "https://github.com/CODARcode/z-checker-installer/archive/refs/tags/0.7.0.tar.gz"
    git      = "https://github.com/robertu94/z-checker-installer"

    maintainers = ['disheng222', 'robertu94']

    version('develop', branch='develop')

    depends_on('libpressio@0.66.3:+sz+zfp+fpzip+json')
    depends_on('z-checker')
    depends_on('perl')
    depends_on('git')
    depends_on('gnuplot@5.0.6:')
    depends_on('libpng@1.6.37:')
    depends_on('tif22pnm')
    depends_on('sam2p')
    depends_on('texlive')
    depends_on('ghostscript')

    def cmake_args(self):
        args = []
        return args
