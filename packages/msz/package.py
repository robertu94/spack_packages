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
    url = "https://github.com/YuxiaoLi1234/MSz/archive/refs/tags/v0.0.2.tar.gz"
    git = "https://github.com/YuxiaoLi1234/MSz"

    maintainers("YuxiaoLi1234", "robertu94")

    license("MIT", checked_by="robertu94")

    version("main", branch="main")
    version("0.0.2", sha256="7f88bf29b6ab7035246173c59b5fa6e3c6b31cab53e5b241530ae7bf72befa13")
    version("0.0.1", sha256="504bed79593ec7605a4a3c63cb038163e9de6fea8f8d75487001612e83bd9073")
    


    variant("zstd", default=True, description="Enable Zstd compression")
    variant("cuda", default=False, description="Enable CUDA support")
    variant("openmp", default=False, description="Enable OpenMP for parallelism")

    depends_on("zstd build_system=cmake", when="+zstd")
    depends_on("cuda", when="+cuda")
    depends_on("cmake@3.19:", type="build", when="+zstd")

    def cmake_args(self):
        args = []
        if "+cuda" in self.spec:
            args.append("-DENABLE_CUDA=ON")
        else:
            args.append("-DENABLE_CUDA=OFF")

        if "+openmp" in self.spec:
            args.append("-DENABLE_OPENMP=ON")
        else:
            args.append("-DENABLE_OPENMP=OFF")

        if "+zstd" in self.spec:
            args.append("-DENABLE_ZSTD=ON")
        else:
            args.append("-DENABLE_ZSTD=OFF")

        return args
