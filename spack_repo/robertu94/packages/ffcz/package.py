# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Ffcz(CMakePackage):
    """FFCz: Fast Fourier Correction for Error-Bounded Lossy Compression"""

    homepage = "https://github.com/rcrcarissa/FFCz"
    url = "https://github.com/rcrcarissa/FFCz/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/rcrcarissa/FFCz.git"

    maintainers("rcrcarissa", "guoxiliu", "robertu94")

    license("MIT")

    version("1.0.0", sha256="bfba21711fa8c5b3cb686e453c12c887614b63c6108bda0c9e7f146eabe571fe", preferred=True)
    version("main", branch="main")

    root_cmakelists_dir = "CPU"

    depends_on("cmake@3.18:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("fftw precision=float,double", type=("build", "link"))
    depends_on("zstd", type=("build", "link"))

    @run_after("install")
    def create_ffcz_symlink(self):
        ffcz_cpu = join_path(self.prefix.bin, "ffcz_cpu")
        ffcz_bin = join_path(self.prefix.bin, "ffcz")
        if os.path.exists(ffcz_cpu) and not os.path.exists(ffcz_bin):
            symlink(ffcz_cpu, ffcz_bin)

