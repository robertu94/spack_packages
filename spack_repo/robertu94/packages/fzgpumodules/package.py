# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *

class Fzgpumodules(CMakePackage, CudaPackage):
    """FZGPUModules: A GPU-accelerated module library for prediction-based
    error-bounded lossy compression, providing composable pipeline stages
    (predictors, encoders, memory management) via a DAG-driven compressor."""

    # package info
    homepage = "https://szcompressor.org/"
    # url = "https://github.com/szcompressor/FZModules/releases/download/1.0.0/fzmodules-1.0.0.tar.gz"
    git = "https://github.com/szcompressor/FZModules.git"

    maintainers("skyler-ruiter")

    license("BSD-3-Clause", checked_by="skyler-ruiter")

    # versions
    version("1.0", branch="refactor")

    # dependencies
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cuda", type=("build", "link", "run"))

    # conflicts
    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda")

    # build targets
    variant("shared", default=True, description="Build shared libraries")

    # CMake options
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BUILD_TESTING", False),
            self.define("BUILD_PROFILING", False),
            self.define(
                "CMAKE_CUDA_ARCHITECTURES",
                self.spec.variants["cuda_arch"].value,
            ),
        ]
        return args
