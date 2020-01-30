# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
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
#     spack install py-m
#
# You can edit this file again by typing:
#
#     spack edit py-m
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyM(PythonPackage):
    """A build automation tool"""

    homepage = "https://github.com/robertu94/m"
    git      = "https://github.com/robertu94/m"

    version('master', branch="master")

    extends('python@3.6:')
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('cmake', type='run')
    depends_on('ninja', type='run')
    depends_on('autotools', type='run')
