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
#     spack install r-libpressio
#
# You can edit this file again by typing:
#
#     spack edit r-libpressio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RLibpressio(RPackage):
    """R package for libpressio"""

    homepage = "https://github.com/robertu94/libpressio-r"
    url      = "https://github.com/robertu94/libpressio-r/archive/0.0.1.tar.gz"

    # notify when the package is updated.
    maintainers = ['robertu94']

    version('1.2', sha256='e5889abf6aabd14b25b5c11e8ecc42cfe56681b1e4f7ade9c9fc28de213981b4')
    version('1.1', sha256='b86a541e095b6e41b3548f6cd734c1ff50c70edda2806ed66b5205880fbfbb96')
    version('0.0.1', sha256='a508cf3ec1b06c417e0de0e1e4180f3175ead2e4ec23b374425fcf2abfaa1b88')

    # FIXME: Add dependencies if required.
    depends_on('r@3.3.0:', type=('build','run'))
    depends_on('r-rcpp', type=('build', 'link', 'run'))
    depends_on('libpressio+json', type=('build', 'link', 'run'))
    depends_on('libpressio@0.65.0:+json', type=('build', 'link', 'run'), when="@1.2:")
    depends_on('pkgconfig', type=('build'))
