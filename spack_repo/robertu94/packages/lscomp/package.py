# Copyright Spack Project Developers. See COPYRIGHT file for details.
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
#     spack install lscomp
#
# You can edit this file again by typing:
#
#     spack edit lscomp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack.package import *


class Lscomp(CMakePackage, CudaPackage):
    """a specialized lossy and lossless compressor for light sources"""

    homepage = "https://szcompressor.com"
    git = "https://github.com/hyfshishen/SC25-lsCOMP"
    url = "https://github.com/hyfshishen/SC25-lsCOMP"

    root_cmakelists_dir = "lsCOMP"

    maintainers("hyfshishen", "robertu94")

    license("BSD-4-Clause", checked_by="robertu94")

    variant("examples", description="build the example CLI programs", default=True)
    variant("shared", description="build a shared library", default=True)

    version("1.0.0", commit="5b0834b4ddfb7951edc252467294ef2c7ace9951")

    conflicts("~cuda", msg="requires cuda to build")

    depends_on("cmake@3.21:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")

    def cmake_args(self):
        cuda_arch = self.spec.variants["cuda_arch"].value
        args = [
                "-DBUILD_TESTING=OFF",
                self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
                self.define_from_variant("cuLSZ_BUILD_EXAMPLES", "examples"),
                ("-DCMAKE_CUDA_ARCHITECTURES=%s" % cuda_arch)
        ]
        return args

