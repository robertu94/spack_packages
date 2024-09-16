# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.cusz import Cusz as BuiltinCusz


class Cusz(BuiltinCusz):
    """A GPU accelerated error-bounded lossy compression for scientific data"""

    git = "https://github.com/robertu94/cusz"
    version("streams", branch="feature-omp-ms")
    depends_on("python", type=("build", "link", "run"), when="@streams")
