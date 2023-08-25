# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class LibpressioPredict(CMakePackage):
    """High Fidelity Proxy Models for Compression"""

    homepage = "https://github.com/robertu94/libpressio-predict"
    url = "https://github.com/robertu94/libpressio-predict/archive/refs/tags/0.0.0.tar.gz"
    git = "https://github.com/robertu94/libpressio-predict"

    maintainers("robertu94")

    version("0.0.2", sha256="02323e03c832cd1f116136347c6b2b52e5c04485fcd57aeb588b6f1923c62a60")
    version("0.0.0", sha256="b3c08be05e3b49542929e4d3849c232d1343c66c9f785b312bb37196dc530035")

    variant("bin", default=True, description="build the command line tools")
    variant("shared", default=True, description="build shared libaries")


    depends_on("libpressio-tools@0.4.2:")
    depends_on("libpressio@0.96.3:")
    depends_on("libpressio-dataset@0.0.6:", when="@0.0.2:")
    with when("+bin"):
        depends_on("libpressio+libdistributed+json+remote+mpi+openssl")
        depends_on("libdistributed@0.4.3:")
        depends_on("mpi")
        depends_on("sqlite@3.38:+dynamic_extensions")
        depends_on("libpressio-dataset@0.0.5", when="@0.0.0")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("LIBPRESSIO_PREDICT_BUILD_TOOLS", "bin"),
            self.define("LIBPRESSIO_PREDICT_USE_MPI", self.spec.satisfies("^ mpi")),
        ]
        return args
