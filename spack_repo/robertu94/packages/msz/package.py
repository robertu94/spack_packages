# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
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
        args = [
                self.define_from_variant("MSZ_ENABLE_ZSTD", "zstd"),
                self.define_from_variant("MSZ_ENABLE_OPENMP", "openmp"),
                self.define_from_variant("MSZ_ENABLE_CUDA", "cuda"),
        ]
        if "+cuda" in self.spec:
            cuda_arch_list = self.spec.variants["cuda_arch"].value
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", cuda_arch_list))

        return args
