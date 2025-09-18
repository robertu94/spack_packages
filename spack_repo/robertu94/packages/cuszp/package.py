# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *


class Cuszp(CMakePackage, CudaPackage):
    """cuSZp is an ultra-fast and user-friendly GPU error-bounded lossy compressor for floating-point data"""

    homepage = "https://szcompressor.org/"
    url = "https://github.com/szcompressor/cuSZp/releases/download/cuSZp-V2.0/cuSZp-V2.0.zip"
    git = "https://github.com/szcompressor/cuSZp"

    maintainers("robertu94", "hyfshishen")

    license("BSD-3-Clause", checked_by="robertu94")

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda")

    variant("examples", description="build the examples", default=True)
    version("2.0.1", commit="47c8f51aeaa1b82293b2f723c17cecf4c239c921", git="https://github.com/robertu94/cuSZp")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("cuSZp_BUILD_EXAMPLES","examples"),
            ("-DCMAKE_CUDA_ARCHITECTURES=%s" % self.spec.variants["cuda_arch"].value)
        ]
        return args
