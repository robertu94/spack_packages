# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ---------------------------------------------------------------------------- If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-ldcpy
#
# You can edit this file again by typing:
#
#     spack edit py-ldcpy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyLdcpy(PythonPackage):
    """Statistical and visual tools for gathering metrics and comparing Earth System Model data files. A common use case is comparing data that has been lossily compressed with the original data."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://ldcpy.readthedocs.io/"
    url      = "https://files.pythonhosted.org/packages/d7/60/67075b7643d0f8ca5aa3198ab883ca7b6cc49935389d30545cf168c8be91/ldcpy-0.16-py3-none-any.whl"

    version('0.16', sha256='d787c21044e433b3da28bb196840ad49a278f2a01ac054cde5f3ded5c9a9bb22', expand=False)

    depends_on('py-setuptools', type='build')

    depends_on('py-scikit-image', type=('build', 'run'))
    depends_on('py-cartopy', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-dask', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-xarray', type=('build', 'run'))
    depends_on('py-cf-xarray', type=('build', 'run'))
    depends_on('py-statsmodels', type=('build', 'run'))
    depends_on('py-pooch', type=('build', 'run'))
    depends_on('py-xrft', type=('build', 'run'))
    depends_on('py-cftime', type=('build', 'run'))
    depends_on('py-cmocean', type=('build', 'run'))

