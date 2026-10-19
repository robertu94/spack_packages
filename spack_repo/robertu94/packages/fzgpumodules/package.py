# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *


class Fzgpumodules(CMakePackage, CudaPackage):
    """Composable CUDA compression pipelines for scientific data."""

    homepage = "https://szcompressor.org/"
    git = "https://github.com/szcompressor/FZGPUModules.git"

    maintainers("skyler-ruiter")

    license("BSD-3-Clause", checked_by="skyler-ruiter")

    version(
        "2.0.1",
        url="https://github.com/szcompressor/FZGPUModules/archive/refs/tags/v2.0.1.tar.gz",
        sha256="c18a9a06a0742a66a8345edca8d38b5b3c96633db55861e71a40e8609cea14a8",
        preferred=True,
    )
    version(
        "2.0.0",
        url="https://github.com/szcompressor/FZGPUModules/releases/download/v2.0.0/FZGPUModules-2.0.0-source.tar.gz",
        sha256="fe54bec71b0b83033a3e9653f61898ce2c893ca9cefffc8d6c2d621faab70335",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.24:", type="build")
    depends_on("cuda@11.2:", type=("build", "link", "run"))

    conflicts("~cuda")
    conflicts("cuda_arch=none", when="+cuda")

    variant("shared", default=True, description="Build shared libraries")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("BUILD_TESTING", False),
            self.define("BUILD_PROFILING", False),
            self.define("BUILD_CLI", False),
            self.define("BUILD_EXAMPLES", False),
            self.define("FZGMOD_BACKEND", "CUDA"),
            self.define(
                "CMAKE_CUDA_ARCHITECTURES",
                self.spec.variants["cuda_arch"].value,
            ),
        ]
        return args