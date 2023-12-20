# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.sz3 import Sz3 as Sz3Builtin


class Sz3(Sz3Builtin):
    """SZ3 is the next generation of the SZ compressor framework"""

    version("artifact", git="https://github.com/lxAltria/SZ3", branch="artifact_mitigation")
    version("3.1.8", commit="e308ebf8528c233286874b920c72c0a6c0218fb2")
