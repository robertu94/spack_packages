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
#     spack install py-cf-xarray
#
# You can edit this file again by typing:
#
#     spack edit py-cf-xarray
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyCfXarray(PythonPackage):
    """A lightweight convenience wrapper for using CF attributes on xarray objects"""

    homepage = "https://cf-xarray.readthedocs.io/en/latest/"
    pypi     = "cf_xarray/cf_xarray-0.7.2.tar.gz"

    version('0.7.2', sha256='4677c3788152dbe5472b0553a7ded31190c85b254eabd269820f70f76c61a78d')

    depends_on('py-xarray', type=('build', 'run'))

    depends_on('py-setuptools', type='build')
