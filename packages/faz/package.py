# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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
#     spack install faz
#
# You can edit this file again by typing:
#
#     spack edit faz
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *

class Faz(CMakePackage):
    """A flexible auto-tuned modular error-bounded compression framework for scientific data"""

    homepage = "https://github.com/JLiu-1/FAZ"
    url = "ssh://git@github.com/JLiu-1/FAZ"
    git = "git@github.com:JLiu-1/FAZ"

    maintainers("JLiu-1", "robertu94")

    license("BSD-3-Clause", checked_by="robertu94")

    version("0.1.0", commit="e2cabff9e8002d89d5e30003cf25f042cb322e51")

    depends_on("python@3.6:")
    depends_on("py-numpy")
    depends_on("py-pybind11")
    depends_on("py-pywavelets")
    depends_on("zstd")

