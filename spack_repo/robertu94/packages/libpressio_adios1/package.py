# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class LibpressioAdios1(CMakePackage):
    """LibPressio file reader for legacy ADIOS1 files not supported by ADIOS2"""

    homepage = "https://github.com/robertu94/libpressio-adios1"
    url = "https://github.com/robertu94/libpressio-adios1/archive/refs/tags/0.0.1.tar.gz"
    git = "https://github.com/robertu94/libpressio-adios1"

    maintainers("robertu94")

    version("0.0.3", sha256="ea6919e8f67a37e892ee3a1044798d772e7826e06ef8b3b2df83aee2ad8f49ec")
    version("0.0.2", sha256="cb3c4ef3c9c3bd5f4c08d1145a07d2ce0c84605a2213b744992c6c8cef998d39")

    depends_on("adios")
    depends_on("libpressio")

    def cmake_args(self):
        args = [
            self.define("CMAKE_MODULE_PATH", self.spec["adios"].prefix.etc),
            self.define("BUILD_TESTING", self.run_tests),
        ]
        return args
