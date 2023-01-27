# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Mpigdb(Package):
    """Open Source Parallel Debugger Built on GDB for MPI"""

    homepage = "https://github.com/robertu94/mpigdb"
    url = "https://github.com/robertu94/mpigdb/archive/refs/tags/0.2.0.tar.gz"
    git = "https://github.com/robertu94/mpigdb"

    maintainers = ["robertu94"]

    version("0.2.0", sha256="ac134422b11b40af6567489986535133391154e83960d6cac53f9cf37c26c1ec")

    depends_on("rust@1.65:", type=("build"))
    depends_on("gdb+python@12.1:", type=("run"))
    depends_on("python@3.8:", type=("run"))
    depends_on("mpi", type=("run"))

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", prefix, "--path", ".")

