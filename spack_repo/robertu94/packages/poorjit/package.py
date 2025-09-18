# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Poorjit(CMakePackage):
    """A poorman's JIT library"""

    homepage = "https://github.com/robertu94/poorjit"
    url = "https://github.com/robertu94/poorjit/archive/refs/tags/0.0.2.tar.gz"
    git = "https://github.com/robertu94/poorjit"

    maintainers("robertu94")

    license("BSD-4-Clause", checked_by="robertu94")

    version("0.0.3", sha256="0ac8b450563fdc988384fba2ac563dcc7e7e74f53c88f538d48aa83461a3bdb5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("boost+filesystem@:1.87") # TODO boost process 1.88 requires a different header path
    depends_on("zlib")
    depends_on("fmt")

    def cmake_args(self):
        args = [
            "-DPOORJIT_DEFAULT_COMPILER=%s" % self.compiler.cxx
        ]
        return args
