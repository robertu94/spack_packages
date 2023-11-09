# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
#     spack install lc-framework
#
# You can edit this file again by typing:
#
#     spack edit lc-framework
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class LcFramework(CMakePackage):
    """a framework for automatically creating high-speed lossless and error-bounded lossy data compression and decompression algorithms."""

    homepage = "https://userweb.cs.txstate.edu/~burtscher/LC/"
    url = "https://github.com/robertu94/LC-framework/archive/refs/tags/1.1.1.tar.gz"
    git = "https://github.com/robertu94/LC-framework"

    maintainers("robertu94")

    version("1.1.1", sha256="4d6f30a489cbcfde9ac48316a15ffbd83576a79235dd6d0e24b42a85b1afe40a")

    variant("libpressio", description="build a libpressio plugin for LC", default=False)

    depends_on("python", type=("build",))
    depends_on("libpressio@0.98.0:", when="+libpressio")

    def cmake_args(self):
        args = [
            self.define_from_variant("LC_BUILD_LIBPRESSIO_PLUGIN", "libpressio")
        ]
        return args
