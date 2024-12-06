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
#     spack install msz
#
# You can edit this file again by typing:
#
#     spack edit msz
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Msz(CMakePackage, CudaPackage):
    """An Efficient Parallel Algorithm for Correcting Morse-Smale Segmentations in Error-Bounded Lossy Compressors"""

    homepage = "https://github.com/YuxiaoLi1234/MSz"
    url = "https://github.com/YuxiaoLi1234/MSz/archive/refs/tags/v0.0.1.tar.gz"
    git = "https://github.com/YuxiaoLi1234/MSz"

    maintainers("YuxiaoLi1234", "robertu94")

    license("MIT", checked_by="robertu94")

    version("0.0.1", sha256="504bed79593ec7605a4a3c63cb038163e9de6fea8f8d75487001612e83bd9073")

    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    depends_on("zfp")
    depends_on("sz3")
    depends_on("zstd")
    conflicts("~cuda")

    def cmake_args(self):
        args = [
            self.define_cuda_architectures(self)
        ]

        return args
