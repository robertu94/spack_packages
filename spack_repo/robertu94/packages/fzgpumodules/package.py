# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *


class Fzgpumodules(CMakePackage, CudaPackage):
    """FZGPUModules: GPU-accelerated graph composable compression 
        pipeline builder for analytical workflows."""

    homepage = "https://szcompressor.org/"
    git = "https://github.com/szcompressor/FZModules.git"

    maintainers("skyler-ruiter")

    license("BSD-3-Clause", checked_by="skyler-ruiter")

    version("2.0", branch="main")
    version("1.0", branch="refactor")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cuda", type=("build", "link", "run"))

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda")

    variant("shared", default=True, description="Build shared libraries")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BUILD_TESTING", False),
            self.define("BUILD_PROFILING", False),
            self.define("BUILD_CLI", False),
            self.define(
                "CMAKE_CUDA_ARCHITECTURES",
                self.spec.variants["cuda_arch"].value,
            ),
        ]
        return args