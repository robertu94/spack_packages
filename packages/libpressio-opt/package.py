# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_opt import LibpressioOpt as BuiltinLibpressioOpt


class LibpressioOpt(BuiltinLibpressioOpt):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

    version("0.14.0", sha256="1e8d348f9777f3d49764b22b1f2abefd4b972cb9b1fa27c867373d32c8f1c57d")
    depends_on("libpressio@0.93.0:", when="@0.14.0:")
