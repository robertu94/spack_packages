# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Szp(CMakePackage):
    """ an extreme-fast error-bounded lossy compressor."""

    homepage = "https://www.szcompresor.org"
    url = "https://github.com/szcompressor/SZp/archive/refs/tags/1.1.tar.gz"
    git = "https://github.com/szcompressor/SZp"


    maintainers("robertu94", "disheng222")

    license("MIT", checked_by="robertu94")

    version("1.1", sha256="b1694fe64cdd7743c68924e2099aa3e317bbc9b2133d11fc04159c3d613d2456")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("zstd")

    variant("shared", default=True, description="build shared libraries")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared")
        ]
