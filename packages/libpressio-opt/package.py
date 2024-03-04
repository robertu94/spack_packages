# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_opt import LibpressioOpt as BuiltinLibpressioOpt


class LibpressioOpt(BuiltinLibpressioOpt):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    version("0.15.4", sha256="43ff4a13300eb0812066b193f0883295156c85a5980f225e739f95f029c77f92")

    depends_on("libpressio@0.99.4:", when="@0.15.4:")
