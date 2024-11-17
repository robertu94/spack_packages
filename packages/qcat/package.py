# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Qcat(CMakePackage):
    """Quick data compression quality analysis tool"""

    homepage = "https://github.com/szcompressor/qcat"
    git = "https://github.com/szcompressor/qcat"
    url = "https://github.com/szcompressor/qcat/archive/refs/tags/1.7.tar.gz"

    maintainers("disheng222", "robertu94")

    license("BSD-2-Clause")

    version("master", branch="master")
    version("1.7.1", commit="3c9b580b32e1cde70e15d1399f8fc7c943369bb2", git="https://github.com/robertu94/qcat")
    version("1.7", commit="01f56216f2dd2a5bfe9f9685485e3f8b7ee87e35")
    version("1.4", commit="f16032cf237837b1d32dde0c3daa6ad1ca4a912f")

    depends_on("c", type="build")

    depends_on("zstd")
    depends_on("gnuplot", type="run")

    def cmake_args(self):
        args = ["-DQCAT_USE_BUNDLES=OFF"]
        return args
