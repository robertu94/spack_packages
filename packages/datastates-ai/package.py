# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class DatastatesAi(CMakePackage):
    """"""

    homepage = "https://github.com/DataStates/datastates-ai/"
    url = "https://github.com/DataStates/datastates-ai/"
    git = "ssh://git@github.com/DataStates/datastates-ai/"

    maintainers("robertu94")

    version("main", branch="main")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")
    depends_on("py-nanobind")
    depends_on("mochi-thallium")
    depends_on("py-torch", type="test")

    def cmake_args(self):
        args = [
        ]
        return args
