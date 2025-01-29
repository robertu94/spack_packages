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
    git = "https://github.com/YuxiaoLi1234/MSz"

    maintainers("YuxiaoLi1234", "robertu94")

    license("MIT", checked_by="robertu94")

    version("dev", branch="main")

    variant("zstd", default=True, description="Enable Zstd compression")
    variant("cuda", default=False, description="Enable CUDA support")
    variant("openmp", default=False, description="Enable OpenMP for parallelism")

    depends_on("zstd", when="+zstd")
    depends_on("cuda", when="+cuda")
    depends_on("pkgconfig", type="build", when="+zstd")
    depends_on("cmake@3.19:", type="build")

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
            zstd_prefix = self.spec["zstd"].prefix
            args.append("-DENABLE_ZSTD=ON")

            # Use pkg-config to ensure correct library and include paths
            zstd_lib_dir = f"{zstd_prefix.lib}"
            zstd_include_dir = f"{zstd_prefix.include}"
            args.append(f"-DZSTD_LIBRARY={zstd_lib_dir}/libzstd.so")
            args.append(f"-DZSTD_INCLUDE_DIR={zstd_include_dir}")
        else:
            args.append("-DENABLE_ZSTD=OFF")

        return args
