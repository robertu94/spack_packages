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
#     spack install py-xrft
#
# You can edit this file again by typing:
#
#     spack edit py-xrft
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyXrft(PythonPackage):
    """Fourier transforms for xarray data"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://xrft.readthedocs.io/en/latest/"
    pypi     = "xrft/xrft-0.4.1.tar.gz"

    version('0.4.1', sha256='59a6c93d627de4ef3193e43cc16570789f1b3480731d976ee33666c4d0c29d7b')

    depends_on('py-setuptools', type='build')
    depends_on('py-dask', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-xarray', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
