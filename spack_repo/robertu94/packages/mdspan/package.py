# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install mdspan
#
# You can edit this file again by typing:
#
#     spack edit mdspan
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Mdspan(CMakePackage):
    """Backport of C++23's std::mdspan"""

    homepage = "https://github.com/kokkos/mdspan"
    git = "https://github.com/kokkos/mdspan"

    version("stable", branch="stable")

    depends_on("cmake@3.14:")

    def cmake_args(self):
        args = [
            self.define("MDSPAN_ENABLE_TESTS", self.run_tests),
            self.define("MDSPAN_ENABLE_EXAMPLES", False),
            self.define("MDSPAN_ENABLE_COMP_BENCH", False),
            self.define("MDSPAN_ENABLE_CUDA", False),
            self.define("MDSPAN_ENABLE_OPENMP", False),
            self.define("MDSPAN_USE_SYSTEM_GTEST", False),
        ]
        return args
